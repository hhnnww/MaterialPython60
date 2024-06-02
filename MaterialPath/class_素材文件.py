from pathlib import Path

from pydantic import BaseModel

from .class_文件夹结构 import Class素材文件夹结构
from .class_素材文件信息 import Class素材文件信息


class Model素材单个文件模型(BaseModel):
    path: str
    exists: bool


class Model素材文件模型(BaseModel):
    material_file: str
    preview_image: Model素材单个文件模型
    preview_folder_image: Model素材单个文件模型
    web_folder_image: Model素材单个文件模型


class Class素材文件(Class素材文件夹结构, Class素材文件信息):
    def __init__(self, material_file: Path, root_folder: str) -> None:
        Class素材文件夹结构.__init__(self, root_folder=root_folder)
        Class素材文件信息.__init__(self, material_file=material_file)

    @property
    def model(self):
        return Model素材文件模型(
            material_file=self.material_file.as_posix(),
            preview_image=Model素材单个文件模型(
                path=self.preview_image.as_posix(), exists=self.preview_image.exists()
            ),
            preview_folder_image=Model素材单个文件模型(
                path=self.preview_folder_image.as_posix(),
                exists=self.preview_folder_image.exists(),
            ),
            web_folder_image=Model素材单个文件模型(
                path=self.web_folder_image.as_posix(),
                exists=self.web_folder_image.exists(),
            ),
        )

    @property
    def preview_image(self):
        png_path = self.material_file.with_suffix(".png")
        return png_path

    @property
    def preview_folder_image(self):
        return Path(
            self.preview_image.as_posix().replace(
                self.fun_源文件文件夹.as_posix(), self.fun_预览图文件夹.as_posix()
            )
        )

    @property
    def web_folder_image(self):
        return Path(
            self.preview_folder_image.as_posix().replace(
                self.root_folder.as_posix(), self.fun_web文件夹.as_posix()
            )
        )
