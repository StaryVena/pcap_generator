import os
import time
import random
from smb.SMBConnection import SMBConnection


class SambaClient:

    connection = None
    client_id = 'virtual_client'

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
        self.connection = SMBConnection(self.user_name, self.password, self.client_id, self.system_name)

        # establish the actual connection
        connected = self.connection.connect(ip=self.ip)
        if not connected:
            print('Failed to init connection.')

    def list_shares(self):
        try:
            response = self.connection.listShares()
            self.wait()
            for i in range(len(response)):
                print(response[i].name)
            return response
        except Exception as ex:
            print(ex)

    def list_directory(self, share, path='/'):
        try:
            response = self.connection.listPath(share.name, path)
            self.wait()
            for i in range(len(response)):
                print(response[i].filename)
            return response
        except Exception as ex:
            print(ex)

    def download_file(self, share, path):
        file = open(os.devnull, "wb")
        try:
            info = self.connection.retrieveFile(share, path, file)
            file.close()
            self.wait()
            print('Downloaded ' + str(info[1]) + ' bytes.')
        except Exception as ex:
            print(ex)

    def upload_file(self, share, path, file):
        try:
            self.connection.storeFile(share, path, file)
            self.wait()
        except Exception as ex:
            print(ex)

    def delete_file(self, share, path):
        try:
            info = self.connection.deleteFiles(share, path)
            print('Deleted ' + str(info[1]) + ' bytes.')
            self.wait()
        except Exception as ex:
            print(ex)

    def wait(self):
        if self.randomize:
            interval = random.randint(self.min, self.max)
        else:
            interval = (self.max - self.min)/2

        time.sleep(interval)
