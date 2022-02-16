
import tortoise_methods
import config_telegram
import config_avito

from models import AutoURLs, FlatURLs
from tortoise import run_async
from work import work

if __name__ == '__main__':
    # Создание БД
    run_async(tortoise_methods.init()) # run_async по выполнению всех операций init() завершает автоматически соединение с БД

cycle=0
a=1
while a==1:
    cycle+=1

    run_async(work(
                    config_avito.url_search_auto, 
                    config_avito.title_auto, config_avito.publication_auto, config_avito.view_auto,
                    AutoURLs,
                    config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
                    cycle
    ))
    
    run_async(work(
                    config_avito.url_search_flat, 
                    config_avito.title_flat, config_avito.publication_flat, config_avito.view_flat,
                    FlatURLs,
                    config_telegram.api_token_bot, config_telegram.chat_id_flatchannel,
                    cycle
    ))

