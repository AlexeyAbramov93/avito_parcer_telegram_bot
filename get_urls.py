from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def get_urls(url, params=None):

    options = Options()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe/", options=options )
    driver.implicitly_wait(60)

    try:
        driver.get(url)
        # driver.get('https://auto.ru/ivanovo/cars/bmw/all/')

        page_source = driver.find_elements(By.CLASS_NAME, "iva-item-sliderLink-uLz1v")
        # page_source = driver.find_elements(By.CLASS_NAME, "Link OfferThumb")
        
        urls_list = []
        for i in page_source:
            urls_list.append(i.get_attribute('href'))
            # print(i.get_attribute('href'))

    finally:
        driver.quit()
        print('finally')
        return urls_list


