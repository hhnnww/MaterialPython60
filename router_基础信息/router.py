from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ModelBaseInfo(BaseModel):
    shop_name_list: list[str]


@router.get("/get_base_info", response_model=ModelBaseInfo)
def fun_获取基础信息() -> ModelBaseInfo:
    return ModelBaseInfo(shop_name_list=["小夕素材", "饭桶设计", "泡泡素材"])
