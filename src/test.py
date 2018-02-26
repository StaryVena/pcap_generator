from clients.http_client_chrome import ChromeBrowser

crawler = ChromeBrowser('http://pocasi.uher.in')
crawler.start_crawling()