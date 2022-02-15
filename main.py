from bs4 import BeautifulSoup
import requests
import re
import time
import random
import config
import avito_url

####################################################################################################################################

def get_html(url, params=None):
    """ получение кода страницы """
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    html = requests.get(url, headers=headers, params=params)
    return html

####################################################################################################################################
from models import AutoURLs,AutoURLs_Pydantic
from tortoise import Tortoise, run_async

async def init():
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    await Tortoise.generate_schemas(safe=True)

if __name__ == '__main__':
    run_async(init()) # run_async по выполнению всех операций init() завершает автоматически соединение с БД

# Для нового обращения к базе данных надо заново создавать новое подключение
# На данный момент получилось только так:
# await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})

async def add_to_DB(link):
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    await AutoURLs.create(link=link)

async def get_all_from_DB(link):
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    return await AutoURLs.filter(link=link).count()

####################################################################################################################################

def send_telegram(text):
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(config.api_token), params=dict(
        chat_id='@ivanovo_podbor_auto',
        text=text
    ))

######################################################################################################################

async def work(link, all_titles, all_publications):

    if not await get_all_from_DB(link):
        await add_to_DB(link)

        time.sleep(random.randint(20, 30)) # Сон на несколько секунд
        soup_link = BeautifulSoup((get_html(temp_link)).text, "html.parser")
        metadata_views=soup_link.find_all('div', class_=re.compile('title-info-metadata-item title-info-metadata-views'))
        try:
            views=int([i for i in (metadata_views[0].text).split()][0])
        except Exception as ex:
            views=0
            print(ex)

        if views<500:
            text=str(all_titles[i].get('title')) + '\n' + str(temp_link) + '\n' 'Просмотров: ' + str(views) + "  (" + str(all_publications[i].text) + ')'
            send_telegram(text)   

######################################################################################################################

all_titlesars=[]
all_publications=[]

a=1
count=0
while a==1:
    count+=1
    avito_page=get_html(avito_url.url)
    soup = BeautifulSoup(avito_page.text, "html.parser")


    # Составляю списки из необходимых заголовков
    all_titles = soup.find_all('a', class_=re.compile('link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'))
    all_publications = soup.find_all('div', class_=re.compile('date-text'))

    # Обрабатываю списки поэлементно и забираю нужные данные
    for i in range(len(all_titles)):
        print(i+1, 'from', len(all_titles))
        temp_link='https://www.avito.ru'+str(all_titles[i].get('href'))

        run_async(work(temp_link,all_titles,all_publications))
    
    print('-------------------------------------------------------------------------------------------')
    print('Проход №{} | Ответ сервера: {} {}'.format(count, avito_page.status_code, avito_page.reason))
    print('-------------------------------------------------------------------------------------------')

    time.sleep(random.randint(60*4, 60*7)) # Сон на несколько минут

######################################################################################################################

