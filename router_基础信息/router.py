from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Model基础信息模型(BaseModel):
    shop_name_list: list[str]


@router.get("/get_base_info", response_model=Model基础信息模型)
def fun_获取基础信息() -> Model基础信息模型:
    return Model基础信息模型(shop_name_list=["小夕素材", "饭桶设计", "泡泡素材"])
