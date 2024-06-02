from functools import cached_property

from .class_共用功能 import Class公共功能
from .class_文件夹结构 import Class素材文件夹结构
from .class_素材文件 import Class素材文件


class Class素材文件夹(Class素材文件夹结构, Class公共功能):
    def __init__(self, root_folder: str) -> None:
        Class素材文件夹结构.__init__(self, root_folder=root_folder)

    @cached_property
    def fun_所有素材文件(self) -> list[Class素材文件]:
        return [
            Class素材文件(material_file=obj, root_folder=self.root_folder.as_posix())
            for obj in self.fun_遍历文件夹(
                self.fun_源文件文件夹, self.material_suffix_list
            )
        ]

    @property
    def fun_所有素材文件后缀排序(self):
        self.fun_所有素材文件.sort(key=lambda k: k.format_level)
        return self.fun_所有素材文件
