import os
from os.path import join
from selenium import webdriver
from pathlib import Path
from clients.http_client_selenium import SeleniumBrowser


class ChromeBrowser(SeleniumBrowser):
    window_width = 1200
    window_height = 600

    def __init__(self, index, wait_interval=10, page_load_interval=5):
        SeleniumBrowser.__init__(self, index, wait_interval, page_load_interval)

    def init_driver(self):
        act_dir = os.path.dirname(__file__)
        data_dir = join(str(Path(act_dir).parent.parent), 'data')

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size='+str(self.window_width)+'x'+str(self.window_height))

        chromedriver_path = join(data_dir, 'chromedriver')
        print(chromedriver_path)
        driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        return driver
