import time
from bs4 import BeautifulSoup as Soup
import urllib
from urllib.parse import urljoin
from urllib import request

from http_client import HttpClient

tags = ['img', 'embed', 'link', 'script']
attributes = ['src', 'href']

# http://selenium-python.readthedocs.io/api.html
class UrllibDownloader(HttpClient):
    """
    Using Python's urllib for web crawling and downloading.
    :param wait_interval: Defines how many seconds wait before processing next page.
    :param download_content: If true, alse CSS, images, and scripts are downloaded.
    """
    timeout = 5
    def __init__(self, wait_interval=10, download_content=False):
        HttpClient.__init__(self, wait_interval)
        self.download_content = download_content

    def end(self):
        # no need to close anything.
        pass

    def page_links(self, link):
        content = request.urlopen(link, timeout=self.timeout).read().decode("utf-8")
        html = Soup(content, 'html.parser')
        hrefs = [urljoin(link, a['href']) for a in html.find_all('a')]
        # downloading page content

        if self.download_content:
            # TODO
            #response = HtmlResponse(url=link, body=content, encoding='utf8')
            with urllib.request.urlopen(link) as response:
                html = response.read()


            #extractor = LxmlParserLinkExtractor(lambda x: x in tags, lambda x: x in attributes)
            #resource_urls = [urljoin(link, l.url) for l in extractor.extract_links(response)]
            #for content_link in resource_urls:
            #    try:
            #        self.links_visited += 1
            #        self.download_file(content_link)
            #    except:
            #        self.links_problem += 1
            #        print('Problem resolving content ' + str(content_link))
        self.wait()
        return hrefs

    def download_file(self, link):
        '''
        Downloads and discards given file.
        :param link: URL of resource to be downloaded.
        '''
        self.log.debug('Downloading ' + link)
        request.urlopen(link, timeout=self.timeout).read()
