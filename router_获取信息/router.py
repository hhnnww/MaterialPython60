from fastapi import APIRouter
from pydantic import BaseModel

from MaterialPath.class_素材文件 import ModelMaterialFile

from .class_上下文件夹 import ModelPrevAndNext
from .class_素材信息 import MaterialFolderInfo, ModelFormat

router = APIRouter()


class ItemIn(BaseModel):
    root_path: str


class ItemOut(BaseModel):
    format: ModelFormat
    size_title: str

    near_folder: ModelPrevAndNext

    all_material: list[ModelMaterialFile]


@router.post("/get_material_info", response_model=ItemOut)
def fun_获取素材信息(item_in: ItemIn) -> ItemOut:
    mfi = MaterialFolderInfo(root_folder=item_in.root_path)

    return ItemOut(
        format=mfi.comb_one_format,
        size_title=mfi.size_title,
        near_folder=mfi.near_folder_model,
        all_material=[obj.model for obj in mfi.all_material_obj],
    )
