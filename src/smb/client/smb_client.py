import os
import io
import uuid
from smb.SMBConnection import SMBConnection

CLIENT_NAME = 'admin'
CLIENT_P = 'oGenTen5'
SYSTEM_NAME = 'NAS'


class SambaClient:

    connection = None
    client_id = 'virtual_client'

    def __init__(self, user_name, password, system_name, ip=''):
        self.user_name = user_name
        self.password = password
        self.system_name = system_name
        self.ip = system_name
        if len(ip) > 0:
            self.ip = ip

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
            for i in range(len(response)):
                print(response[i].name)
            return response
        except Exception as ex:
            print(ex)

    def list_directory(self, share, path='/'):
        try:
            response = self.connection.listPath(share.name, path)
            for i in range(len(response)):
                print(response[i].filename)
            return response
        except Exception as ex:
            print(ex)

    def download_file(self, share, path):
        file = open(os.devnull, "wb")
        try:
            info = self.connection.retrieveFile(share, path, file)
            print('Downloaded ' + str(info[1]) + ' bytes.')
            file.close()
        except Exception as ex:
            print(ex)

    def upload_file(self, share, path, file):
        try:
            self.connection.storeFile(share, path, file)
        except Exception as ex:
            print(ex)


def main():
    client = SambaClient(CLIENT_NAME, CLIENT_P, SYSTEM_NAME, '192.168.88.2')
    shares = client.list_shares()
    dir = 'Pictures'
    files = client.list_directory(shares[0], path=dir)
    client.download_file(shares[0].name, dir+'/'+files[4].filename)
    f = io.BytesIO(os.urandom(200*1024))
    file_name = 'gen_'+str(uuid.uuid4())+'.txt'
    client.upload_file(shares[0].name, dir+'/'+file_name, f)


if __name__ == "__main__":
    main()
