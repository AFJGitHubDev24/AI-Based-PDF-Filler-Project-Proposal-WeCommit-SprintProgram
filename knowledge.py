from fastapi import APIRouter, HTTPException
from tortoise.transactions import in_transaction
from app.models import KnowledgeBase_Pydantic, KnowledgeBaseIn_Pydantic, KnowledgeBase
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()

@router.post("/", response_model=KnowledgeBase_Pydantic)
async def create_knowledge_base_item(item: KnowledgeBaseIn_Pydantic):
    obj = await KnowledgeBase.create(**item.dict())
    return await KnowledgeBase_Pydantic.from_tortoise_orm(obj)

@router.get("/", response_model=list[KnowledgeBase_Pydantic])
async def get_all_knowledge_base_items():
    return await KnowledgeBase_Pydantic.from_queryset(KnowledgeBase.all())

@router.get("/{item_id}", response_model=KnowledgeBase_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_knowledge_base_item(item_id: int):
    obj = await KnowledgeBase_Pydantic.from_queryset_single(KnowledgeBase.get(id=item_id))
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return obj

@router.put("/{item_id}", response_model=KnowledgeBase_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_knowledge_base_item(item_id: int, item: KnowledgeBaseIn_Pydantic):
    async with in_transaction():
        await KnowledgeBase.filter(id=item_id).update(**item.dict())
        return await KnowledgeBase_Pydantic.from_queryset_single(KnowledgeBase.get(id=item_id))

@router.delete("/{item_id}", response_model=dict, responses={404: {"model": HTTPNotFoundError}})
async def delete_knowledge_base_item(item_id: int):
    delete_count = await KnowledgeBase.filter(id=item_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
