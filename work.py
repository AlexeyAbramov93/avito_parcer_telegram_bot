import tortoise_methods
from bs4 import BeautifulSoup
import re
import time
import random

import config_telegram
import send_telegram
from get_html import get_html
from send_telegram import send_telegram

import urllib


async def work(url_search_auto, title_auto, publication_auto, view_auto, modelURLs, api_token_bot, chat_id, cycle):

    search_page=get_html(url_search_auto)
    website=urllib.parse.urlsplit(url_search_auto).netloc
    #print(website, search_page.status_code)

    log_msg=('#{}: {} {}'.format(cycle, search_page.status_code, website))
    send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, log_msg)   

    soup = BeautifulSoup(search_page.text, "html.parser")

    # Составляю списки из необходимых заголовков
    all_titles = soup.find_all('a', class_=re.compile(title_auto))
    all_publications = soup.find_all('div', class_=re.compile(publication_auto))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        
        tmp_link= {
            'www.avito.ru':'https://www.avito.ru'+str(all_titles[i].get('href')),
            'ivanovo.cian.ru': str(all_titles[i].get('href'))
        }

        if not await tortoise_methods.get_all_from_DB(modelURLs, tmp_link[website]):
            section_avito='avtomobili'
            if 'kvartiry' in url_search_auto:
                section_avito='kvartiry'
            section = {'www.avito.ru' : section_avito, 'www.auto.ru' : 'avtomobili', 'ivanovo.cian.ru' : 'kvartiry'}
            await tortoise_methods.add_to_DB(modelURLs, tmp_link[website], website, section[website])

            time.sleep(random.randint(30, 60)) # Сон на несколько секунд между перебором новых объявлений
            if website=='www.avito.ru':
                soup_link = BeautifulSoup((get_html(tmp_link[website])).text, "html.parser")
                metadata_views=soup_link.find_all('div', class_=re.compile(view_auto))
                try:
                    views=int([i for i in (metadata_views[0].text).split()][0])
                except Exception as ex:
                    views=0
                    print(ex)
                if views<1000:
                    text=str(all_titles[i].get('title')) + '\n' + str(tmp_link[website]) + '\n' 'Просмотров: ' + str(views) + "  (" + str(all_publications[i].text) + ')'
                    send_telegram(api_token_bot, chat_id, text)   
                    #print('-----------------------------')
                    #print(text)
            elif website=='ivanovo.cian.ru':
                text=tmp_link[website]
                send_telegram(api_token_bot, chat_id, text)
                #print('-----------------------------')
                #print(text)
        #print('{} из {}'.format(i+1, len(all_titles)))

    time.sleep(random.randint(1*60, 2*60)) # Сон на несколько минут


