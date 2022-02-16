import tortoise_methods
from bs4 import BeautifulSoup
import re
import time
import random

import config_telegram
import send_telegram
from get_html import get_html
from send_telegram import send_telegram


async def work(url_search_auto, title_auto, publication_auto, view_auto, modelURLs, api_token_bot, chat_id, cycle):

    search_page=get_html(url_search_auto)

    log_msg=('#{}: {} {} {}'.format(cycle, search_page.status_code, search_page.reason, str(modelURLs)))
    send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, log_msg)   

    soup = BeautifulSoup(search_page.text, "html.parser")

    # Составляю списки из необходимых заголовков
    all_titles = soup.find_all('a', class_=re.compile(title_auto))
    all_publications = soup.find_all('div', class_=re.compile(publication_auto))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        tmp_link='https://www.avito.ru'+str(all_titles[i].get('href'))

        if not await tortoise_methods.get_all_from_DB(modelURLs, tmp_link):
            await tortoise_methods.add_to_DB(modelURLs, tmp_link)

            time.sleep(random.randint(10, 15)) # Сон на несколько секунд между перебором новых объявлений
            soup_link = BeautifulSoup((get_html(tmp_link)).text, "html.parser")
            metadata_views=soup_link.find_all('div', class_=re.compile(view_auto))
            try:
                views=int([i for i in (metadata_views[0].text).split()][0])
            except Exception as ex:
                views=0
                print(ex)

            if views<750:
                text=str(all_titles[i].get('title')) + '\n' + str(tmp_link) + '\n' 'Просмотров: ' + str(views) + "  (" + str(all_publications[i].text) + ')'
                send_telegram(api_token_bot, chat_id, text)   

        #print('{} из {}'.format(i+1, len(all_titles)))

    time.sleep(random.randint(30, 40)) # Сон на несколько минут


async def work_cian(url_search_auto, title_auto, modelURLs, api_token_bot, chat_id, cycle):

    search_page=get_html(url_search_auto)

    log_msg=('#{}: {} {} {}'.format(cycle, search_page.status_code, search_page.reason, str(modelURLs)))
    send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, log_msg)   

    soup = BeautifulSoup(search_page.text, "html.parser")

    # Составляю списки из необходимых заголовков
    all_titles = soup.find_all('a', class_=re.compile(title_auto))
    #all_publications = soup.find_all('div', class_=re.compile(publication_auto))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        tmp_link=str(all_titles[i].get('href'))

        if not await tortoise_methods.get_all_from_DB(modelURLs, tmp_link):
            await tortoise_methods.add_to_DB(modelURLs, tmp_link)

            time.sleep(5) # Сон на несколько секунд между перебором новых объявлений
            # soup_link = BeautifulSoup((get_html(tmp_link)).text, "html.parser")
            # metadata_views=soup_link.find_all('div', class_=re.compile(view_auto))
            # try:
            #     views=int([i for i in (metadata_views[0].text).split()][0])
            # except Exception as ex:
            #     views=0
            #     print(ex)

            # if views<750:
            text=tmp_link
            send_telegram(api_token_bot, chat_id, text)   

        #print('{} из {}'.format(i+1, len(all_titles)))

    time.sleep(random.randint(30, 40)) # Сон на несколько минут