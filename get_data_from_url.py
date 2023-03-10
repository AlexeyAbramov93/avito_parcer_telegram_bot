from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_data_from_url(url, params=None):

    options = Options()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe/", options=options )
    driver.implicitly_wait(60)

    price_info=''

    try:
        driver.get(url)
        # <span class="desktop-ged5cz">250&nbsp;000&nbsp;₽ — соответствует Авито Оценке</span>
        price_info = driver.find_element(By.CLASS_NAME, "desktop-ged5cz").text

    finally:
        print('finally')
        driver.quit()
        return price_info