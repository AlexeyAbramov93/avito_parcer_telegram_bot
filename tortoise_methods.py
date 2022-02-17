
from tortoise import Tortoise, run_async
from tortoise.models import Model

from models import AbstractBase#, Advertisement, Section, Website

async def init():
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    await Tortoise.generate_schemas(safe=True)

# Для нового обращения к базе данных надо заново создавать новое подключение
# На данный момент получилось только так:
# await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
async def add_to_DB(AbstractBase, link):
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    await AbstractBase.create(link=link)

async def get_all_from_DB(AbstractBase, link):
    await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
    return await AbstractBase.filter(link=link).count()


# ############################################################################################################################################################
# # Для новой структуры базы данных
# ############################################################################################################################################################
    
# async def init():
#     await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
#     await Tortoise.generate_schemas(safe=True)

#     await Section.create(name='avtomobili')
#     await Section.create(name='kvartiry')

#     await Website.create(name='www.avito.ru')
#     await Website.create(name='www.auto.ru')
#     await Website.create(name='ivanovo.cian.ru')

# async def add_to_DB(Advertisement, link, section, website):
#     await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
#     await Advertisement.create(link=link, section=section, website=website)

# async def get_all_from_DB(Advertisement, link):
#     await Tortoise.init(db_url='sqlite://sql_app.db', modules={'models': ['__main__']})
#     return await Advertisement.filter(link=link).count()