from fastapi import APIRouter
from pydantic import BaseModel

from class_material_path import ModelEffectImage, ModelMaterialFile

from .class_素材信息 import ClassMaterialInfo, ModelMateiralItemFormat

router = APIRouter()


class ItemIn(BaseModel):
    root_path: str


class ItemOut(BaseModel):
    size: str
    prev_path: str
    next_path: str
    format_list: list[ModelMateiralItemFormat]
    all_material: list[ModelMaterialFile]
    all_effect: list[ModelEffectImage]


@router.post("/get_info", response_model=ItemOut)
def get_info(item_in: ItemIn) -> ItemOut:
    cla_material_info = ClassMaterialInfo(root_path=item_in.root_path)

    return ItemOut(
        prev_path=cla_material_info.prev_path.as_posix(),
        next_path=cla_material_info.next_path.as_posix(),
        size=cla_material_info.size,
        format_list=list(cla_material_info.all_format_item),
        all_material=[obj.model for obj in cla_material_info.sort_materials("num")],
        all_effect=[obj.model for obj in cla_material_info.all_effect_image],
    )
