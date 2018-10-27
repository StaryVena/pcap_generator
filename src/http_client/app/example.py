import logging.config
from http_client_wget import WgetDownloader
from http_client_urllib import UrllibDownloader
from http_client_selenium import SeleniumBrowser

CHROME = 'chrome'
WGET = 'wget'
URLLIB = 'urllib'


def get_crawler(crawler_type):
    if crawler_type == CHROME:
        return SeleniumBrowser()
    elif crawler_type == WGET:
        return WgetDownloader()
    elif crawler_type == URLLIB:
        return UrllibDownloader()


page = 'http://pocasi.uher.in'
crawler = get_crawler(CHROME)
crawler.start_crawling(page)
