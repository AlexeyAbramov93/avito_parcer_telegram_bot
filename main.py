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

url='https://www.avito.ru/ivanovo/avtomobili/inomarki/benzin-ASgBAQICAUTgtg2kijQBQOy2DRTetyg?cd=1&f=ASgBAQECAUTgtg2kijQBQOy2DRTetygDRfgCFnsiZnJvbSI6OTAwLCJ0byI6bnVsbH28FRh7ImZyb20iOjE1Nzg2LCJ0byI6bnVsbH3GmgwXeyJmcm9tIjowLCJ0byI6MTAwMDAwMH0&radius=0&user=1'
status_code=(get_html(url)).status_code
reason=(get_html(url)).reason
print(status_code, reason)

all_titlesars=[]
all_prices=[]
all_publications=[]
link_list=[] # На основе этого списка определяется объявление уже было добавлено или нет

for i in range(5):
    print('-----------------------------------------------------------------------')
    print("ПРОХОД НОМЕР", i)
    print('-----------------------------------------------------------------------')

    soup = BeautifulSoup((get_html(url)).text, "html.parser")

    # Составляю списки из необходимых заголовков
    # all_titles = soup.find_all('h3', class_=re.compile('title-root'))
    # all_prices = soup.find_all('div', class_=re.compile('iva-item-priceStep'))
    # all_publications = soup.find_all('div', class_=re.compile('date-text'))
    # all_href = soup.find_all('a', class_=re.compile('iva-item-sliderLink'))

    all_titles = soup.find_all('a', class_=re.compile('link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'))
    all_publications = soup.find_all('div', class_=re.compile('date-text'))
    #all_href = soup.find_all('a', class_=re.compile('iva-item-sliderLink'))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        print(i+1, 'from', len(all_titles))
        temp_link='https://www.avito.ru'+str(all_titles[i].get('href'))
        
        if temp_link not in link_list:
            link_list.append(temp_link)

            time.sleep(random.randint(10, 15)) # Сон на несколько секунд
            soup_link = BeautifulSoup((get_html(temp_link)).text, "html.parser")
            metadata_views=soup_link.find_all('div', class_=re.compile('title-info-metadata-item title-info-metadata-views'))
            views=int([i for i in (metadata_views[0].text).split()][0])

            if views<1500:
                print('{}'.format(all_titles[i].get('title')))
                print(temp_link)
                print('Количество просмотров: {}   |   {}'.format(views, all_publications[i].text))
                print()

    time.sleep(random.randint(20, 30)) # Сон на несколько секунд

######################################################################################################################

