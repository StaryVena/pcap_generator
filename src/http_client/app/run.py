import time
import logging.config
from argparse import ArgumentParser


CHROME = 'chrome'
WGET = 'wget'
URLLIB = 'urllib'


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('console')
# logging.getLogger('clients.http_client_urllib.UrllibDownloader').addHandler()
# logging.basicConfig(level=logging.DEBUG)


def get_crawler(crawler_type):
    if crawler_type == CHROME:
        from http_client_selenium import SeleniumBrowser
        return SeleniumBrowser()
    elif crawler_type == WGET:
        from http_client_wget import WgetDownloader
        return WgetDownloader()
    elif crawler_type == URLLIB:
        from http_client_urllib import UrllibDownloader
        return UrllibDownloader()
    else:
        from http_client_urllib import UrllibDownloader
        return UrllibDownloader()


parser = ArgumentParser()
parser.add_argument("-p", "--page", dest="page", help="URL address to crawl.", metavar="URL", required=True)
parser.add_argument("-c", "--crawler", dest="crawler", help="Define crawler (chrome/wget/urllib)",
                    metavar="URL", required=False, default='urllib')

args = parser.parse_args()
time.sleep(5)
crawler = get_crawler(args.crawler)
crawler.start_crawling(args.page)
