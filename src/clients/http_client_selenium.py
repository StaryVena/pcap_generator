import abc
import time
from clients.http_client import HttpClient


# http://selenium-python.readthedocs.io/api.html
class SeleniumBrowser(HttpClient):

    def __init__(self, index, wait_interval=10, page_load_interval=5):
        HttpClient.__init__(self, index, wait_interval)
        self.driver = self.init_driver()
        # wait up to wait_interval seconds for the elements to become available
        self.driver.implicitly_wait(page_load_interval)

    @abc.abstractmethod
    def init_driver(self):
        """Create browser specific driver (chrome, firefox, etc)"""
        return

    def page_links(self, link):
        self.driver.get(link)
        links = self.driver.find_elements_by_tag_name('a')
        hrefs = []
        for link in links:
            url = link.get_attribute("href")
            if HttpClient.is_link_ok(url):
                hrefs.append(url)
        time.sleep(self.wait_interval)
        return hrefs

    def close_driver(self):
        self.driver.quit()
