import time
import random

import tortoise_methods
import config_telegram
import config_avito

from models import Advertisement, Section, Website

from tortoise import run_async
from work import work

from send_telegram import send_telegram

if __name__ == '__main__':
    # Создание БД
    run_async(tortoise_methods.init()) # run_async по выполнению всех операций init() завершает автоматически соединение с БД

cycle=0
a=1
while a==1:
    try:
        cycle+=1
        run_async(work(
                        config_avito.url_search_auto, 
                        config_avito.title_auto, config_avito.publication_auto, config_avito.view_auto,
                        Advertisement,
                        config_telegram.api_token_bot, config_telegram.chat_id_autochannel,
                        cycle
        ))
        
        run_async(work(
                        config_avito.url_search_flat, 
                        config_avito.title_flat, config_avito.publication_flat, config_avito.view_flat,
                        Advertisement,
                        config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
                        cycle
        ))

        run_async(work(
                        config_avito.url_search_flat_cian, 
                        config_avito.title_flat_cian, config_avito.publication_auto, config_avito.view_auto,
                        Advertisement,
                        config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
                        cycle
        ))

    except Exception as ex:
        send_telegram(config_telegram.api_token_bot, config_telegram.chat_id_exceptions,ex)   
        #print(ex)

    time.sleep(random.randint(15, 20)) # Сон на несколько секунд


