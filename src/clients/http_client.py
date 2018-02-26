import os
from os.path import join
import time
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By

# http://selenium-python.readthedocs.io/api.html
act_dir = os.path.dirname(__file__)
data_dir = join(str(Path(act_dir).parent.parent), 'data')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

chromedriver_path = join(data_dir, 'chromedriver')
print(chromedriver_path)
driver = webdriver.Chrome(chromedriver_path, chrome_options=options)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
# wait up to 10 seconds for the elements to become available
driver.implicitly_wait(10)
links = driver.find_elements_by_tag_name('a')
for link in links:
    url = link.get_attribute("href")
    print(url)

time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
