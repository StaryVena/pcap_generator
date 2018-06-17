import os
from os.path import join
from selenium import webdriver
from pathlib import Path


def chrome_driver(window_width=1200, window_height=600):
    """
    Loads Chrome driver. Chrome or Chromium must be installed.
    :return: Loaded Chrome driver.
    """
    act_dir = os.path.dirname(__file__)

    options = webdriver.ChromeOptions()
    # do not show window
    options.add_argument('headless')
    # disable GPU
    options.add_argument('disable-gpu')
    # page view window size
    options.add_argument('window-size=' + str(window_width) + 'x' + str(window_height))

    driver = webdriver.Chrome(join(act_dir, 'chromedriver'), chrome_options=options)
    return driver
