import abc
import logging

LIST_MAXIMUM_LENGTH = 200

class HttpClient(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, index, wait_interval):
        self.index = index
        self.wait_interval = wait_interval

    @abc.abstractmethod
    def page_links(self, link):
        """Returns all valid urls from actual page."""
        return

    @abc.abstractmethod
    def end(self):
        """clean up"""
        return

    def start_crawling(self):
        links = [self.index]
        while len(links) > 0:
            links.extend(self.page_links(links.pop(0)))
            if len(links) > LIST_MAXIMUM_LENGTH:
                links = links[:LIST_MAXIMUM_LENGTH/2]
        self.end()

    def is_link_ok(link):
        print(link)
        # empty href
        if link is None:
            logging.debug(link + ' BAD')
            return False
        # javascript action
        if link.startswith('javascript'):
            logging.debug(link + ' BAD')
            return False
        # TODO relative link
        # otherwise is OK
        logging.debug(link + ' OK')
        return True