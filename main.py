from bs4 import BeautifulSoup
import re
import time
import random

import tortoise_methods

import get_html

import config_telegram
import send_telegram

import config_avito

from models import AutoURLs, FlatURLs
from tortoise import run_async

####################################################################################################################################

async def work(modelURLs, link, all_titles, all_publications):

    if not await tortoise_methods.get_all_from_DB(modelURLs, link):
        await tortoise_methods.add_to_DB(modelURLs, link)

        time.sleep(random.randint(10, 15)) # Сон на несколько секунд
        soup_link = BeautifulSoup((get_html.get_html(temp_link)).text, "html.parser")
        metadata_views=soup_link.find_all('div', class_=re.compile(config_avito.view_auto))
        try:
            views=int([i for i in (metadata_views[0].text).split()][0])
        except Exception as ex:
            views=0
            print(ex)

        if views<500:
            text=str(all_titles[i].get('title')) + '\n' + str(temp_link) + '\n' 'Просмотров: ' + str(views) + "  (" + str(all_publications[i].text) + ')'
            send_telegram.send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,text)   

######################################################################################################################

if __name__ == '__main__':
    # Создание БД
    run_async(tortoise_methods.init()) # run_async по выполнению всех операций init() завершает автоматически соединение с БД

a=1
count=0
while a==1:
    count+=1
    avito_page=get_html.get_html(config_avito.url_search_auto)
    soup = BeautifulSoup(avito_page.text, "html.parser")

    # Составляю списки из необходимых заголовков
    all_titles = soup.find_all('a', class_=re.compile(config_avito.title_auto))
    all_publications = soup.find_all('div', class_=re.compile(config_avito.publication_auto))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        print(i+1, 'from', len(all_titles))
        temp_link='https://www.avito.ru'+str(all_titles[i].get('href'))

        run_async(work(AutoURLs, temp_link,all_titles,all_publications))
    
    print('-------------------------------------------------------------------------------------------')
    print('Проход №{} | Ответ сервера: {} {}'.format(count, avito_page.status_code, avito_page.reason))
    print('-------------------------------------------------------------------------------------------')

    time.sleep(random.randint(60*4, 60*7)) # Сон на несколько минут

######################################################################################################################

