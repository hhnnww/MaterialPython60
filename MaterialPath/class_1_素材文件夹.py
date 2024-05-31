from functools import cached_property

from .class_共用功能 import BaseFunction
from .class_文件夹结构 import MaterialFolderStructure
from .class_素材文件 import MaterialFile


class MaterialFolder(MaterialFolderStructure, BaseFunction):
    def __init__(self, root_folder: str) -> None:
        MaterialFolderStructure.__init__(self, root_folder=root_folder)

    @cached_property
    def all_material_obj(self) -> list[MaterialFile]:
        return [
            MaterialFile(material_file=obj, root_folder=self.root_folder.as_posix())
            for obj in self.fun_遍历文件夹(
                self.material_folder, self.material_suffix_list
            )
        ]

    @property
    def all_material_obj_sort_by_format(self):
        self.all_material_obj.sort(key=lambda k: k.format_level)
        return self.all_material_obj
