import time
import random

import tortoise_methods
import config_telegram
import config_avito

from models import Advertisement#, Section, Website

from tortoise import run_async
from work import work

from send_telegram import send_telegram

if __name__ == '__main__':
    # Создание БД
    run_async(tortoise_methods.init()) # run_async по выполнению всех операций init() завершает автоматически соединение с БД

cycle=0
a=1
while a==1:
    cycle+=1
    
    run_async(work(
                    config_avito.url_search_auto_at, 
                    config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
                    Advertisement,
                    config_telegram.api_token_bot, config_telegram.chat_id_autochannel_at,
                    cycle
    ))

    run_async(work(
                    config_avito.url_search_auto_mt, 
                    config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
                    Advertisement,
                    config_telegram.api_token_bot, config_telegram.chat_id_autochannel_mt,
                    cycle
    ))

    # run_async(work(
    #                 config_avito.url_search_noutbuki, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_notechannel,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_velo, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_velochannel,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_kolesa_R15, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_kolesa_R16, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_shiny_R15, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_shiny_R16, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_shiny_R17, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_shiny_R18, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_kolesa,
    #                 cycle
    # ))

    run_async(work(
                    config_avito.url_search_zapchasti_getz, 
                    config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
                    Advertisement,
                    config_telegram.api_token_bot, config_telegram.chat_id_avtosvet,
                    cycle
    ))
    
    # run_async(work(
    #                 config_avito.url_search_flat_cian, 
    #                 config_avito.title_flat_cian, config_avito.price_cian, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_flat_cian_rent, 
    #                 config_avito.title_flat_cian, config_avito.price_cian, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_flatchannel_rent,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_flat, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_flat_rent, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_flatchannel_rent,
    #                 cycle
    # ))




    run_async(work(
                    config_avito.url_search_zapchasti_ceed, 
                    config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
                    Advertisement,
                    config_telegram.api_token_bot, config_telegram.chat_id_zapchasti_ceed,
                    cycle
    ))

    run_async(work(
                    config_avito.url_search_zapchasti_ceed_rest, 
                    config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
                    Advertisement,
                    config_telegram.api_token_bot, config_telegram.chat_id_zapchasti_ceed,
                    cycle
    ))

    # run_async(work(
    #                 config_avito.url_search_PK, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_PK,
    #                 cycle
    # ))

    # run_async(work(
    #                 config_avito.url_search_PK2, 
    #                 config_avito.title_avito, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    #                 Advertisement,
    #                 config_telegram.api_token_bot, config_telegram.chat_id_PK,
    #                 cycle
    # ))



















    # # # AUTO.RU
    # # run_async(work(
    # #                 config_avito.url_search_auto2, 
    # #                 config_avito.title_auto_ru, config_avito.price_avito, config_avito.publication_avito, config_avito.view_avito,
    # #                 Advertisement,
    # #                 config_telegram.api_token_bot, config_telegram.chat_id_auto_cx5,
    # #                 cycle
    # # ))
    

