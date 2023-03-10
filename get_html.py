from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def get_html(url, params=None):

    options = Options()
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe/", options=options )

    driver.implicitly_wait(10)

    try:
        driver.get('https://www.avito.ru/ivanovo/avtomobili?cd=1&radius=200')
        # print(f'Title: "{driver}"')
        # page_source = driver.find_element(By.TAG_NAME, "body").text

        page_source = driver.find_elements(By.CLASS_NAME, "iva-item-sliderLink-uLz1v")
        for i in page_source:
            print(i.get_attribute('href'))


    finally:
        driver.quit()
        print('finally')