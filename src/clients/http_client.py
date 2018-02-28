import abc
import logging
import validators
from random import shuffle

# maximum urls queue length
LIST_MAXIMUM_LENGTH = 200


class HttpClient(object):
    __metaclass__ = abc.ABCMeta
    """
    Meta class for all classes which works with HTTP web crawling. Class instance downloads web page,
    finds links and visits next page from urls list.
    :param wait_interval: Defines how many seconds wait before processing next page.
    """
    def __init__(self, wait_interval):
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())
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
        while len(links) > 0:
            new_links = self.page_links(links.pop(0))
            # randomly shuffle links
            shuffle(links)
            links.extend(new_links)
            # if queue is too long, limit to half.
            if len(links) > LIST_MAXIMUM_LENGTH:
                links = links[:LIST_MAXIMUM_LENGTH/2]
        self.end()

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
            logging.debug(link + ' BAD')
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
