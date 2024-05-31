from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse
from PIL import Image

from MaterialPath.class_素材文件 import MaterialFile

router = APIRouter()


@router.get("/image")
def fun_获取图片(material_file: str, root_path: str):
    mf = MaterialFile(material_file=Path(material_file), root_folder=root_path)

    if mf.web_folder_image.exists() is False:
        if mf.web_folder_image.parent.exists() is not True:
            mf.web_folder_image.parent.mkdir(parents=True)

        with Image.open(mf.preview_folder_image.as_posix()) as im:
            im.thumbnail((500, 500))
            im.save(mf.web_folder_image.as_posix())

    return FileResponse(path=mf.web_folder_image)
