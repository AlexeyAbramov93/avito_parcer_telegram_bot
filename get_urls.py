from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_urls(url, params=None):

    options = Options()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe/", options=options )
    driver.implicitly_wait(60)

    data_list = []

    try:
        driver.get(url)

        urls = driver.find_elements(By.CLASS_NAME, "iva-item-sliderLink-uLz1v")
        prices = driver.find_elements(By.CLASS_NAME, "iva-item-priceStep-uq2CQ")
        comment = driver.find_elements(By.CLASS_NAME, "SnippetLayout-root-d2alh")

        for i in range(len(urls)):
            data_list.append({
                'href': urls[i].get_attribute('href'), 
                'price': prices[i].text,
                'comment': comment[i].text
                })
    finally:
        print('finally')
        driver.quit()
        return data_list


