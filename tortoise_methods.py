
from tortoise import Tortoise, run_async
from tortoise.models import Model

from models import AbstractBase

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
