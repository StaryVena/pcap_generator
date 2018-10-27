from selenium import webdriver


def chrome_driver(window_width=1420, window_height=1080):
    """
    Loads Chrome driver. Chrome or Chromium must be installed.
    :return: Loaded Chrome driver.
    """

    chrome_options = webdriver.ChromeOptions()
    # running as root -> must be set this
    chrome_options.add_argument('"--no-sandbox"')
    # page view window size
    chrome_options.add_argument('window-size=' + str(window_width) + ',' + str(window_height))
    # do not show window
    chrome_options.add_argument('headless')
    # disable GPU
    chrome_options.add_argument('disable-gpu')

    driver = webdriver.Chrome(chrome_options=chrome_options)

    return driver
