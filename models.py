from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class AutoURLs(Model):
    id = fields.IntField(pk=True)
    link=fields.TextField()
    
    class Meta:
        table = 'AutoURLs'
        table_description = 'This table saves unique AutoURLs history'

    def __str__(self):
        return self.name

AutoURLs_Pydantic = pydantic_model_creator(AutoURLs, name="AutoURLs")

