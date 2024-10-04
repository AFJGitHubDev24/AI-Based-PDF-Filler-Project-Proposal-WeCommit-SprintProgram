from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class KnowledgeBase(Model):
    id = fields.IntField(pk=True)
    field_name = fields.CharField(max_length=255)
    value = fields.TextField()

    class Meta:
        table = "knowledge_base"

    def __str__(self):
        return self.field_name

# Pydantic models for serialization
KnowledgeBase_Pydantic = pydantic_model_creator(KnowledgeBase, name="KnowledgeBase")
KnowledgeBaseIn_Pydantic = pydantic_model_creator(KnowledgeBase, name="KnowledgeBaseIn", exclude_readonly=True)
