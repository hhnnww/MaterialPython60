from fastapi import APIRouter
from pydantic import BaseModel

from MaterialPath.class_素材文件 import ModelMaterialFile

from .class_上下文件夹 import Model上下文件夹模型
from .class_素材信息 import Class素材文件夹信息, Model素材格式信息

router = APIRouter()


class Model素材信息请求模型(BaseModel):
    root_path: str


class Model素材信息模型(BaseModel):
    format: Model素材格式信息
    size_title: str

    near_folder: Model上下文件夹模型

    all_material: list[ModelMaterialFile]


@router.post("/get_material_info", response_model=Model素材信息模型)
def fun_获取素材信息(item_in: Model素材信息请求模型) -> Model素材信息模型:
    mfi = Class素材文件夹信息(root_folder=item_in.root_path)

    return Model素材信息模型(
        format=mfi.comb_one_format,
        size_title=mfi.size_title,
        near_folder=mfi.near_folder_model,
        all_material=[obj.model for obj in mfi.all_material_obj],
    )
