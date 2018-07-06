import abc
import time
import logging
import logging.handlers
import validators
import uuid
from random import shuffle, randint

# maximum urls queue length
LIST_MAXIMUM_LENGTH = 1000


class HttpClient(object):
    __metaclass__ = abc.ABCMeta
    """
    Meta class for all classes which works with HTTP web crawling. Class instance downloads web page,
    finds links and visits next page from urls list.
    :param wait_interval: Defines how many seconds wait before processing next page.
    """
    start_url = None
    links_visited = 0
    links_problem = 0
    client_id = uuid.uuid4()

    def __init__(self, wait_interval):
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.handlers.RotatingFileHandler('/tmp/http_client.log'))
        self.log.setLevel(logging.INFO)
        self.wait_interval = wait_interval

    @abc.abstractmethod
    def page_links(self, link):
        """
        Downloads web page and parse all URLs.
        :param link: URL of web page to process.
        :returns list of URL links from processed web page.
        """
        raise NotImplementedError

    def end(self):
        """This method is called when all ULRs are processed."""
        pass

    def start_crawling(self, index):
        """
        Start up method for running web crawler.
        :param index: URL where crawling starts.
        """
        links = []
        if self.is_link_ok(index):
            links.append(index)
        else:
            self.log.warning("Invalid link "+index)
        if self.start_url is None:
            self.start_url = index
        while len(links) > 0:
            link_to_process = links.pop(0)
            self.links_visited += 1
            try:
                new_links = self.page_links(link_to_process)
                for url in new_links:
                    if not url.startswith(self.start_url):
                        new_links.remove(url)
                        # randomly shuffle links
                shuffle(new_links)
                links.extend(new_links)
                # if queue is too long, limit to half.
                if len(links) > LIST_MAXIMUM_LENGTH:
                    links = links[:LIST_MAXIMUM_LENGTH // 2]
            except Exception as e:
                print(e)
                self.log.debug('Problem processing '+link_to_process)
                self.links_problem += 1
            self.log.info(str(self.client_id) + ' status - problems: ' + str(self.links_problem) +  ' from: ' +
                          str(self.links_visited))


        self.end()


    def wait(self):
        time.sleep(randint(1, self.wait_interval))

    @staticmethod
    def is_link_ok(link):
        """
        Check the link if it contains valid URL.
        :param link:
        :return: True if it is valid URL address. False otherwise.
        """
        print(link)
        # empty href
        if link is None:
            logging.debug('Empty link - BAD')
            return False
        # javascript action
        if link.startswith('javascript'):
            logging.debug(link + ' BAD')
            return False
        # regular expression check
        if not validators.url(link):
            logging.debug(link + ' BAD')
            return False
        # otherwise is OK
        logging.debug(link + ' OK')
        return True
