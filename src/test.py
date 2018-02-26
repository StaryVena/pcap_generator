from clients.http_client_chrome import ChromeBrowser
from clients.http_client_wget import WgetDownloader

CHROME = 'chrome'
WGET = 'wget'

url = 'http://pocasi.uher.in'

type = WGET
crawler = None
if type == CHROME:
    crawler = ChromeBrowser(url)
elif type == WGET:
    crawler = WgetDownloader(url)
crawler.start_crawling()