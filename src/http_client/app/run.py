import logging.config
from argparse import ArgumentParser
from http_client_wget import WgetDownloader
from http_client_urllib import UrllibDownloader
from http_client_selenium import SeleniumBrowser

CHROME = 'chrome'
WGET = 'wget'
URLLIB = 'urllib'


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('console')
#logging.getLogger('clients.http_client_urllib.UrllibDownloader').addHandler()
#logging.basicConfig(level=logging.DEBUG)


def get_crawler(crawler_type):
    if crawler_type == CHROME:
        return SeleniumBrowser()
    elif crawler_type == WGET:
        return WgetDownloader()
    elif crawler_type == URLLIB:
        return UrllibDownloader()


parser = ArgumentParser()
parser.add_argument("-p", "--page", dest="page", help="URL address to crawl.", metavar="URL", required=True)

args = parser.parse_args()

crawler = get_crawler(CHROME)
crawler.start_crawling(args.page)
