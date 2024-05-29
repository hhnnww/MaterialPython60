from functools import cached_property
from pathlib import Path
from typing import Generator

from class_material_path.model import MATERIAL_SUFFIX_LIST, SORT_MODE

from .class_素材文件 import ClassMaterialFile


class ClassGetAllMaterialFile:
    def __init__(
        self,
        material_folder: Path,
        preview_folder: Path,
        web_folder: Path,
    ) -> None:
        self.material_folder = material_folder

        self.material_folder = material_folder
        self.preview_folder = preview_folder
        self.web_folder = web_folder

    @cached_property
    def all_material_list(self) -> Generator[ClassMaterialFile]:
        for in_file in self.material_folder.rglob("*"):
            if in_file.is_file() and in_file.suffix.lower() in MATERIAL_SUFFIX_LIST:
                yield ClassMaterialFile(
                    material_file=in_file,
                    material_folder=self.material_folder,
                    preview_folder=self.preview_folder,
                    web_folder=self.web_folder,
                )

    def sort_all_material_list(self, sort: SORT_MODE) -> list[ClassMaterialFile]:
        ma_list = list(self.all_material_list)
        match sort:
            case "num":
                ma_list.sort(key=lambda k: k.num)
            case "suffix":
                ma_list.sort(key=lambda k: k.format_level)

        return ma_list
