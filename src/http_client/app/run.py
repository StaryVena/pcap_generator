import time
from argparse import ArgumentParser
from http_client_selenium import SeleniumBrowser

CHROME = 'chrome'
WGET = 'wget'
URLLIB = 'urllib'




def get_crawler(crawler_type):
    if crawler_type == CHROME:
        from selenium import webdriver
        chrome_options = webdriver.ChromeOptions()
        # running as root -> must be set this
        chrome_options.add_argument('--no-sandbox')
        # page view window size
        chrome_options.add_argument('window-size=1420,1080')
        # do not show window
        chrome_options.add_argument('headless')
        # disable GPU
        chrome_options.add_argument('disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return SeleniumBrowser(driver=driver)

    elif crawler_type == WGET:
        print('Selected wget as client.')
        from http_client_wget import WgetDownloader
        return WgetDownloader()
    elif crawler_type == URLLIB:
        print('Selected URLlib as client.')
        from http_client_urllib import UrllibDownloader
        return UrllibDownloader()
    else:
        print('Using default client - URLlib.')
        from http_client_urllib import UrllibDownloader
        return UrllibDownloader()


parser = ArgumentParser()
parser.add_argument("-p", "--page", dest="page", help="URL address to crawl.", metavar="URL", required=True)
parser.add_argument("-c", "--crawler", dest="crawler", help="Define crawler (chrome/wget/urllib)",
                    metavar="URL", required=False, default='urllib')

args = parser.parse_args()
time.sleep(5)
print('Initializing crawler.')
crawler = get_crawler(args.crawler)
print('Crawler initialized.')
crawler.start_crawling(args.page)
