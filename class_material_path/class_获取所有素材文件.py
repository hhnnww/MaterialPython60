from functools import cached_property
from pathlib import Path

from .class_素材文件 import ClassMaterialFile
from .class_素材文件夹结构 import ClassMaterialStructure
from .fun_遍历文件夹 import fun_遍历文件夹
from .model import MATERIAL_SUFFIX_LIST, SORT_MODE


class ClassGetAllMaterialFile(ClassMaterialStructure):
    def __init__(self, root_path: Path) -> None:
        super().__init__(root_path)

    @cached_property
    def all_material_file(self) -> list[ClassMaterialFile]:
        return [
            ClassMaterialFile(material_file=obj, root_path=self.root_path)
            for obj in fun_遍历文件夹(
                in_path=self.material_folder, suffix_list=MATERIAL_SUFFIX_LIST
            )
        ]

    def sort_materials(self, sort: SORT_MODE = "num") -> list[ClassMaterialFile]:
        ma_list = list(self.all_material_file)
        match sort:
            case "num":
                ma_list.sort(key=lambda k: k.num)
            case "suffix":
                ma_list.sort(key=lambda k: k._format_level)

        return ma_list
