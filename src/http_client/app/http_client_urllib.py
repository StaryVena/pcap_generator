from os import devnull
from bs4 import BeautifulSoup as Soup
from urllib.parse import urljoin
from urllib import request
from requests import get

from http_client import HttpClient

tags = ['img', 'embed', 'link', 'script']
attributes = ['src', 'href']


class UrllibDownloader(HttpClient):
    """
    Using Python's urllib for web crawling and downloading.
    :param wait_interval: Defines how many seconds wait before processing next page.
    :param download_content: If true, alse CSS, images, and scripts are downloaded.
    """
    timeout = 5
    discard_file = open(devnull, "w")

    def __init__(self, wait_interval=10, download_content=True):
        HttpClient.__init__(self, wait_interval)
        self.download_content = download_content

    def end(self):
        self.discard_file.close()

    def page_links(self, link):
        content = get(link, timeout=self.timeout).text
        html = Soup(content, 'html.parser')
        links = html.find_all('a', href=True)
        hrefs = [urljoin(link, a['href']) for a in links]

        # downloading page content
        if self.download_content:
            for tag in tags:
                for page_file in html.findAll(tag):
                    file_link = urljoin(link, page_file.get('src'))
                    print('Downloading content ', file_link)
                    request.urlretrieve(file_link, devnull)

        self.wait()
        return hrefs

    def download_file(self, link):
        '''
        Downloads and discards given file.
        :param link: URL of resource to be downloaded.
        '''
        self.log.debug('Downloading ' + link)
        request.urlopen(link, timeout=self.timeout).read()


if __name__ == '__main__':
    downloader = UrllibDownloader()

    print(downloader.page_links('https://www.seznam.cz'))
