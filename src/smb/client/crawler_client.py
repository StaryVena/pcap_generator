import io
import os
import time
import uuid
from argparse import ArgumentParser
from smb_client import SambaClient
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

        shares = self.client.list_shares()
        for sh in shares:
            if sh.name == share:
                print('Found share {}'.format(sh.name))
                self.share = sh
                break
        if not self.share:
            print('Share {} was now found on the server, exiting.'.format(share))
            exit(1)

        with open('secret_files.txt', 'r') as file:
            content = file.readlines()
            self.secret_files = [x.strip() for x in content]

    def init_client(self, user_name, password, system_name, ip, min, max, randomize):
        print('Creating client.')
        client = SambaClient(user_name, password, system_name, ip, min, max, randomize)
        print('Client created.')
        self.client = client

    def start(self):
        print('Starting crawling.')
        self.dirs = self.client.list_directory(self.share, path='/')
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
                self.client.download_file(self.share, file)
            elif action == UPLOAD_FILE:
                directory = self.select_directory()
                f = io.BytesIO(os.urandom(200 * 1024))
                file_name = PREFIX + str(uuid.uuid4()) + '.txt'
                print('Uploading file.')
                self.client.upload_file(self.share, directory.filename + '\\' + file_name, f)
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
        files = self.client.list_directory(self.share, directory.filename)
        random.shuffle(files)
        for file in files:
            if not file.isDirectory:
                return directory.filename + '\\' + file.filename

    def delete_random_file(self):
        directory = self.select_directory()
        files = self.client.list_directory(self.share, directory.filename)
        random.shuffle(files)
        for file in files:
            if file.filename.startswith(PREFIX):
                self.client.delete_file(self.share, directory.filename + '\\' + file.filename)

    def try_download_file(self):
        self.client.download_file(self.share, random.choice(self.secret_files))


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

