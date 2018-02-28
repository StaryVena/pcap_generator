import abc
import time
from clients.http_client import HttpClient
from clients.headless_browsers import chrome_driver


class SeleniumBrowser(HttpClient):
    """
    Class for headless web browsers like Chrome, Firefox, etc.
    # http://selenium-python.readthedocs.io/api.html
    :param wait_interval: Defines how many seconds wait before processing next page.
    :param page_load_interval: browser waits for a maximum of defined seconds for page to be loaded and then continues.
    """
    def __init__(self, wait_interval=10, page_load_interval=5, driver=chrome_driver()):
        HttpClient.__init__(self, wait_interval)
        self.driver = driver
        # wait up to wait_interval seconds for the elements to become available
        self.driver.implicitly_wait(page_load_interval)

    @abc.abstractmethod
    def init_driver(self):
        """Create browser specific driver (chrome, firefox, etc)"""
        raise NotImplementedError()

    def page_links(self, link):
        """
        Downloads defined url from link with content like images, css, JavaScript, then parse all urls in a href tags.
         and return it as list.
        :param link: web page to be processed
        :return: list of parsed urls.
        """
        self.driver.get(link)
        links = self.driver.find_elements_by_tag_name('a')
        hrefs = []
        for link in links:
            url = link.get_attribute("href")
            if HttpClient.is_link_ok(url):
                hrefs.append(url)
        time.sleep(self.wait_interval)
        return hrefs

    def end(self):
        """
        Close initialized web browser.
        """
        self.driver.quit()
