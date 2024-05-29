from pathlib import Path

from .class_预览图文件 import ClassPreviewImage
from .fun_获取数字 import fun_获取数字
from .model import IMAGE_SUFFIX_LIST


class ClassMaterialFile(ClassPreviewImage):
    def __init__(
        self,
        material_file: Path,
        material_folder: Path,
        preview_folder: Path,
        web_folder: Path,
    ) -> None:
        self.material_file = material_file

        self.material_folder = material_folder
        self.preview_folder = preview_folder
        self.web_folder = web_folder

        ClassPreviewImage.__init__(
            self,
            preview_image=self.preview_image,
            material_folder=self.material_folder,
            preview_folder=self.preview_folder,
            web_folder=self.web_folder,
        )

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
    def num(self) -> int:
        return fun_获取数字(self.material_file.stem)

    @property
    def format(self) -> str:
        return self.material_file.suffix.lower().replace(".", "")

    @property
    def format_level(self) -> int:
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
