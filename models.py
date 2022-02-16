from tortoise import fields
from tortoise.models import Model

from abc import ABC,abstractproperty


# Абстрактный класс, для объявления функций Tortoise ORM (add_to_DB и get_all_from_DB)
class AbstractBase(ABC):

    __metaclass__=ABC

    @abstractproperty
    def id(self):
        return fields.IntField(pk=True)
    def link(self):
        return fields.TextField()


# Базовый класс
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





        