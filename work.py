import tortoise_methods
from bs4 import BeautifulSoup
import re
import time
import random

import config_telegram
import send_telegram
from get_html import get_html
from get_urls import get_urls

from send_telegram import send_telegram

import urllib


async def work(url_search, title, price, publication_auto, view_auto, modelURLs, api_token_bot, chat_id, cycle):
    try:
        urls_list=get_urls(url_search)
        for elem in urls_list:
            if not await tortoise_methods.get_all_from_DB(modelURLs, elem):
                await tortoise_methods.add_to_DB(modelURLs, elem)
                # print(elem)
                send_telegram(api_token_bot, chat_id, str(elem))
                time.sleep(5)
        time.sleep(random.randint(5, 10))
    except Exception as ex:
        send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, ex)   
        # print(ex)



    # try:

    #     search_page=get_html(url_search)
    #     website=urllib.parse.urlsplit(url_search).netloc
    #     #print(website, search_page.status_code)

    #     log_msg=('#{}: {} {}'.format(cycle, search_page.status_code, website))
    #     send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, log_msg)   

    #     soup = BeautifulSoup(search_page.text, "html.parser")
    #     #print(soup)

    #     # Составляю списки из необходимых заголовков
    #     all_titles = soup.find_all('a', class_=re.compile(title))
    #     all_publications = soup.find_all('div', class_=re.compile(publication_auto))
    #     all_prices = soup.find_all('span', class_=re.compile(price))
    #     # print(all_titles)
    #     # print(all_publications)
    #     # print(all_prices)

    #     # Обрабатываю списки поэлементно и забираю нужные данные
    #     for i in range(len(all_titles)):

    #         tmp_link= {
    #             'www.avito.ru':'https://www.avito.ru'+str(all_titles[i].get('href')),
    #             'ivanovo.cian.ru': str(all_titles[i].get('href')),
    #             'www.auto.ru': str(all_titles[i].get('href'))
    #         }

    #         if not await tortoise_methods.get_all_from_DB(modelURLs, tmp_link[website]):
                
    #             #####################################
    #             if 'avtomobili' in url_search:
    #                 section_avito='avtomobili'
    #             elif 'kvartiry' in url_search:
    #                 section_avito='kvartiry'
    #             elif 'noutbuki' in url_search:
    #                 section_avito='noutbuki'
    #             else:
    #                 section_avito='other'
    #             #####################################

    #             section = {'www.avito.ru' : section_avito, 'www.auto.ru' : 'avtomobili', 'ivanovo.cian.ru' : 'kvartiry'}
    #             await tortoise_methods.add_to_DB(modelURLs, tmp_link[website], website, section[website])

    #             time.sleep(random.randint(5, 10)) # Сон на несколько секунд между перебором новых объявлений
    #             # if website=='www.avito.ru':
    #             #     soup_link = BeautifulSoup((get_html(tmp_link[website])).text, "html.parser")
    #             #     metadata_views=soup_link.find_all('div', class_=re.compile(view_auto))
    #             #     try:
    #             #         views=int([i for i in (metadata_views[0].text).split()][0])
    #             #     except Exception as ex:
    #             #         views=0
    #             #         #print(ex)
    #             #     if views<3000:
    #             #         text=str(all_titles[i].get('title')) + '\n' + all_prices[i].text + '\n' + str(tmp_link[website]) + '\n' 'Просмотров: ' + str(views) + "  (" + str(all_publications[i].text) + ')'
    #             #         send_telegram(api_token_bot, chat_id, text)   
    #             #         #print('-----------------------------')
    #             #         #print(text)
    #             # elif website=='ivanovo.cian.ru':
    #             #     text=all_prices[i].text + '\n' + tmp_link[website]
    #             #     send_telegram(api_token_bot, chat_id, text)
    #             #     #print('-----------------------------')
    #             #     #print(text)
    #             # else:
    #             #     text=str(tmp_link[website])
    #             #     send_telegram(api_token_bot, chat_id, text)
    #             #     #print('-----------------------------')
    #             #     #print(text)

    #             text=''
    #             if website=='www.avito.ru':
    #                 text=str(all_titles[i].get('title')) + '\n' + all_prices[i].text + '\n' + str(tmp_link[website]) + '\n' + '(' + str(all_publications[i].text) + ')'
    #                 #print('-----------------------------')
    #                 #print(text)
    #             elif website=='ivanovo.cian.ru':
    #                 text=all_prices[i].text + '\n' + tmp_link[website]
    #                 #print('-----------------------------')
    #                 #print(text)
    #             else:
    #                 text=str(tmp_link[website])
    #                 #print('-----------------------------')
    #                 #print(text)
    #             send_telegram(api_token_bot, chat_id, text)
    #         #print(website, '{} из {}'.format(i+1, len(all_titles)))       
    # except Exception as ex:
    #     send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions, ex)   
    #     #print(ex)

    time.sleep(random.randint(5, 15)) # Сон на несколько минут
