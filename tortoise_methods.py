
from tortoise import Tortoise

from models import Advertisement, Section, Website

from models import AbstractBase


async def init():
    # Если БД создана генерируется исключение, если нет - то создаётся БД
    try:
        await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
        await Tortoise.generate_schemas(safe=False) # safe=False генерирует исключ если БД уже создана

        await Section.create(name='avtomobili')
        await Section.create(name='kvartiry')

        await Website.create(name='www.avito.ru')
        await Website.create(name='www.auto.ru')
        await Website.create(name='ivanovo.cian.ru')
    except:
        pass

async def add_to_DB(AbstractBase, link, website, section):
    w=await Website.get(name=website)
    s=await Section.get(name=section)
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    await AbstractBase.create(link=link, website=w, section=s)

async def get_all_from_DB(AbstractBase, link):
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    return await AbstractBase.filter(link=link).count()