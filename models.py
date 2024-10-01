from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel

class KnowledgeBase(Model):
    id = fields.IntField(pk=True)
    field_name = fields.CharField(max_length=255, unique=True)
    value = fields.TextField()

class KnowledgeBaseIn_Pydantic(BaseModel):
    field_name: str
    value: str

class KnowledgeBase_Pydantic(BaseModel):
    id: int
    field_name: str
    value: str

    class Config:
        orm_mode = True
