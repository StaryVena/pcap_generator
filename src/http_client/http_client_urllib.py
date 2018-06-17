import time
import logging
from bs4 import BeautifulSoup as Soup
import urllib
from urllib.parse import urljoin
from urllib import request
from scrapy.http import HtmlResponse
from scrapy.linkextractors.lxmlhtml import LxmlParserLinkExtractor

from http_client import HttpClient


# http://selenium-python.readthedocs.io/api.html
class UrllibDownloader(HttpClient):
    """
    Using Python's urllib for web crawling and downloading.
    :param wait_interval: Defines how many seconds wait before processing next page.
    :param download_content: If true, alse CSS, images, and scripts are downloaded.
    """
    def __init__(self, wait_interval=10, download_content=True):
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())
        HttpClient.__init__(self, wait_interval)
        self.download_content = download_content

    def end(self):
        # no need to close anything.
        pass

    def page_links(self, link):
        opener = urllib.request.FancyURLopener({})
        f = opener.open(link)
        content = f.read()
        html = Soup(content, 'html.parser')
        hrefs = [urljoin(link, a['href']) for a in html.find_all('a')]
        # downloading page content
        if self.download_content:
            response = HtmlResponse(url=link, body=content, encoding='utf8')
            tags = ['img', 'embed', 'link', 'script']
            attributes = ['src', 'href']
            extractor = LxmlParserLinkExtractor(lambda x: x in tags, lambda x: x in attributes)
            resource_urls = [urljoin(link, l.url) for l in extractor.extract_links(response)]
            for link in resource_urls:
                self.download_file(link)
        time.sleep(self.wait_interval)
        return hrefs

    def download_file(self, link):
        '''
        Downloads and discards given file.
        :param link: URL of resource to be downloaded.
        '''
        self.log.info('Downloading ' + link)
        request.urlopen(link).read()
