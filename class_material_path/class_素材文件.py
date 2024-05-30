from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .class_素材文件夹结构 import ClassMaterialStructure
from .fun_获取数字 import fun_获取数字
from .model import IMAGE_SUFFIX_LIST


class ModelMaterialFile(BaseModel):
    material_file: str
    preview_image: Optional[str] = None
    preview_folder_image: Optional[str] = None
    web_folder_image: Optional[str] = None


class ClassMaterialFile(ClassMaterialStructure):
    def __init__(self, material_file: Path, root_path: Path) -> None:
        self.material_file = material_file
        super().__init__(root_path=root_path)

    @property
    def model(self) -> ModelMaterialFile:
        obj = ModelMaterialFile(material_file=self.material_file.as_posix())
        if self.preview_image.exists():
            obj.preview_image = self.preview_image.as_posix()
        if self.preview_folder_image.exists():
            obj.preview_folder_image = self.preview_folder_image.as_posix()
        if self.web_folder_image.exists():
            obj.web_folder_image = self.web_folder_image.as_posix()
        return obj

    @property
    def preview_image(self) -> Path:
        """素材文件夹中的预览图"""
        png_image = self.material_file.with_suffix(".png")
        if png_image.exists() is True:
            return png_image

        for suffix in IMAGE_SUFFIX_LIST:
            image_path = self.material_file.with_suffix(suffix=suffix)
            if image_path.exists() is True:
                return image_path

        return png_image

    @property
    def preview_folder_image(self) -> Path:
        """预览图文件夹中的预览图"""
        return Path(
            self.preview_image.as_posix().replace(
                self.material_folder.as_posix(), self.preview_folder.as_posix()
            )
        )

    @property
    def web_folder_image(self) -> Path:
        """web文件夹中的预览图"""
        return Path(
            self.preview_folder_image.as_posix().replace(
                self.preview_folder.as_posix(), self.web_folder.as_posix()
            )
        )

    @property
    def num(self) -> int:
        return fun_获取数字(self.material_file.stem)

    @property
    def format(self) -> str:
        return self.material_file.suffix.lower().replace(".", "")

    @property
    def _format_level(self) -> int:
        match self.format:
            case ["ai", "eps"]:
                return 0
            case ["psd", "psb"]:
                return 1
            case ["ppt", "pptx"]:
                return 2
        return 9

    @property
    def size(self) -> int:
        return self.material_file.stat().st_size
