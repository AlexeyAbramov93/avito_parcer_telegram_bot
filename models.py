from tortoise import fields
from tortoise.models import Model

from abc import ABC,abstractproperty


# Базовый абстрактный класс, чтобы передать его при описании функции Tortoise ORM
class AbstractBase(ABC):

    __metaclass__=ABC

    @abstractproperty
    def id(self):
        return fields.IntField(pk=True)
    def link(self):
        return fields.TextField()


# Базовый абстрактный класс, чтобы передать его при описании функции Tortoise ORM
class URLs(Model):
    id = fields.IntField(pk=True)
    link=fields.TextField()

    def __str__(self):
        return self.name


# Наследуемая модель для хранения ссылок на авто
class AutoURLs(URLs):
   
    class Meta:
        table = 'AutoURLs'
        table_description = 'This table saves unique AutoURLs history'


# Наследуемая модель для хранения ссылок на квартиры
class FlatURLs(URLs):
    
    class Meta:
        table = 'FlatURLs'
        table_description = 'This table saves unique FlatURLs history'





        