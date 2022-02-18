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


# Класс для хранения ссылок на объявления
class Advertisement(Model):

    id = fields.IntField(pk=True)
    link=fields.TextField()

    website = fields.ForeignKeyField('models.Website', related_name='websites', null=True)
    section = fields.ForeignKeyField('models.Section', related_name='sections', null=True)


    class Meta:
        table = 'Advertisements'
        table_description = 'This table saves unique advertisement URLs'

    def __str__(self):
        return self.name


# Класс для хранения названий досок объявнеий
class Website(Model):

    id = fields.IntField(pk=True)
    name=fields.TextField()

    class Meta:
        table = 'Websites'
        table_description = 'This table saves unique advertisement websites'

    def __str__(self):
        return self.name


# Класс для хранения раздела объявления
class Section(Model):

    id = fields.IntField(pk=True)
    name=fields.TextField()

    class Meta:
        table = 'Sections'
        table_description = 'This table saves unique advertisement sections'

    def __str__(self):
        return self.name




        