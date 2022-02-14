from bs4 import BeautifulSoup
import requests
import re
import time
import random

def get_html(url, params=None):
    """ получение кода страницы """
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    html = requests.get(url, headers=headers, params=params)
    return html

######################################################################################################################

url='https://www.avito.ru/ivanovo/avtomobili/do-1-mln-rubley-ASgCAgECAUXGmgwXeyJmcm9tIjowLCJ0byI6MTAwMDAwMH0?cd=1&f=ASgBAgECAUTgtg2kijQDRfgCFnsiZnJvbSI6ODk5LCJ0byI6bnVsbH28FRh7ImZyb20iOjE1Nzg2LCJ0byI6bnVsbH3GmgwXeyJmcm9tIjowLCJ0byI6MTAwMDAwMH0&radius=50&user=1'

#status_code=(get_html(url)).status_code

all_titlesars=[]
all_prices=[]
all_publications=[]

soup = BeautifulSoup((get_html(url)).text, "html.parser")

all_titles = soup.find_all('h3', class_=re.compile('title-root'))
all_prices = soup.find_all('div', class_=re.compile('iva-item-priceStep'))
all_publications = soup.find_all('div', class_=re.compile('date-text'))
all_href = soup.find_all('a', class_=re.compile('iva-item-sliderLink'))

for i in range(len(all_prices)):
    temp_link='https://www.avito.ru'+str(all_href[i].get('href'))
    time.sleep(random.randint(1, 6)) # Сон на несколько секунд
    soup_link = BeautifulSoup((get_html(temp_link)).text, "html.parser")
    metadata_views=soup_link.find_all('div', class_=re.compile('title-info-metadata-item title-info-metadata-views'))
    views=int([i for i in (metadata_views[0].text).split()][0])

    if views<1500:
        print('-----------------------------------------------------------------')
        print('{} {}'.format(all_titles[i].text, all_prices[i].text))
        print(temp_link)
        print('Количество просмотров: {}   |   {}'.format(views, all_publications[i].text))

######################################################################################################################

