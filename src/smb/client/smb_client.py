import os
import socket
import time
import random
from smb.SMBConnection import SMBConnection


class SambaClient:

    connection = None
    client_id = socket.gethostname()

    def __init__(self, user_name, password, system_name, ip='', min=0, max=60, randomize=True):
        self.user_name = user_name
        self.password = password
        self.system_name = system_name
        self.ip = system_name
        if len(ip) > 0:
            self.ip = ip

        self.min = min
        self.max = max
        self.randomize = randomize

        self.connect()

    def connect(self):
        print('Connecting to server with {} {} {} {} {}'.format(self.user_name, self.password, self.client_id, self.system_name, self.ip))
        self.connection = SMBConnection(self.user_name, self.password, self.client_id, self.system_name)
        print('Connecting to server...')
        # establish the actual connection
        connected = self.connection.connect(ip=self.ip, port=139)
        if not connected:
            print('Failed to init connection.')
        else:
            print('Connection initialized.')

    def list_shares(self):
        try:
            response = self.connection.listShares()
            names = []
            for r in response:
                names.append(r.name)
            print('Shares: {}'.format(names))
            self.wait()
            return response
        except Exception as ex:
            print(ex)

    def list_directory(self, share, path='/'):
        try:
            response = self.connection.listPath(share.name, path)
            names = []
            for r in response:
                names.append(r.filename)
            print('Files: {}'.format(names))
            self.wait()
            return response
        except Exception as ex:
            print(ex)

    def download_file(self, share, path):
        file = open(os.devnull, "wb")
        try:
            info = self.connection.retrieveFile(share.name, path, file)
            file.close()
            print('Downloaded ' + str(info[1]) + ' bytes.')
            self.wait()
        except Exception as ex:
            print(ex)

    def upload_file(self, share, path, file):
        try:
            self.connection.storeFile(share.name, path, file)
            print('File {} uploaded.'.format(path))
            self.wait()
        except Exception as ex:
            print(ex)

    def delete_file(self, share, path):
        try:
            self.connection.deleteFiles(share.name, path)
            print('Deleted file {}'.format(path))
            self.wait()
        except Exception as ex:
            print(ex)

    def wait(self):
        if self.randomize:
            interval = random.randint(self.min, self.max)
        else:
            interval = (self.max - self.min)/2
        time.sleep(interval)

