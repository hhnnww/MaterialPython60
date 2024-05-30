from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

from .class_素材文件夹操作 import ClassMaterialFolderAction
from .文件后缀列表 import AD_FILE_SUFFIX_LIST

router = APIRouter()


class ItemIn(BaseModel):
    root_path: str
    shop_name: str

    path_start_stem: int
    file_start_stem: int

    action: str


@router.post("/action")
def material_action(item_in: ItemIn):
    cla = ClassMaterialFolderAction(root_path=item_in.root_path, action=item_in.action)

    match item_in.action:
        case "移动到根目录":
            for obj in cla.all_material_file_with_action:
                obj.fun_移动到根目录()

        case "文件重命名":
            uuid = str(uuid4())
            num = 1
            for obj in cla.all_material_file_with_action:
                obj.fun_素材重命名(f"{uuid}_{num}")
                num += 1

            num = item_in.file_start_stem
            for obj in cla.all_material_file_with_action:
                obj.fun_素材重命名(f"{item_in.shop_name}({num})")
                num += 1

        case "移动到数字目录":
            for obj in cla.all_material_file_with_action:
                obj.fun_移动到数字目录()

        case "复制到预览图":
            for obj in cla.all_material_file_with_action:
                obj.fun_复制到预览图()

        case "删除广告文件":
            for obj in cla.fun_遍历文件夹(
                in_path=cla.material_folder, suffix_list=AD_FILE_SUFFIX_LIST
            ):
                obj.unlink()
