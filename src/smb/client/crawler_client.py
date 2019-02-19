import io
import os
import uuid
from argparse import ArgumentParser
from smb_client import SambaClient


def normal_crawling(client):
    shares = client.list_shares()
    dir = 'Pictures'
    files = client.list_directory(shares[0], path=dir)
    client.download_file(shares[0].name, dir + '/' + files[4].filename)
    f = io.BytesIO(os.urandom(200 * 1024))
    file_name = 'gen_' + str(uuid.uuid4()) + '.txt'
    client.upload_file(shares[0].name, dir + '/' + file_name, f)


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--type",
                        dest="type",
                        choices=['usual', 'attacker'],
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
                        default=60,
                        required=False,
                        help="Sets maximum backoff interval.")
    args = parser.parse_args()

    client = SambaClient(os.environ['SMB_USER'], os.environ['PASSWORD'], os.environ['SMB_HOSTNAME'], os.environ['IP'])

    if args.type == 'usual':
        normal_crawling(client)


if __name__ == "__main__":
    main()
