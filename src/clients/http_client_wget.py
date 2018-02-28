import time
import shlex
from bs4 import BeautifulSoup as Soup
from subprocess import Popen, PIPE
from urllib.parse import urljoin

from clients.http_client import HttpClient


# http://selenium-python.readthedocs.io/api.html
class WgetDownloader(HttpClient):
    """

    """
    def __init__(self, wait_interval=10):
        HttpClient.__init__(self, wait_interval)

    def close_driver(self):
        # No need to close anything.
        pass

    def page_links(self, link):
        # TODO download images, css, and scripts
        cmd = "wget -q -O - --page-requisites --adjust-extension " + link
        process = Popen(shlex.split(cmd), stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        html = Soup(output, 'html.parser')
        hrefs = [urljoin(link,a['href']) for a in html.find_all('a')]
        time.sleep(self.wait_interval)
        return hrefs