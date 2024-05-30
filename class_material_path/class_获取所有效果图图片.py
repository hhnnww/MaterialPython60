from pathlib import Path

from .class_效果图文件 import ClassEffectImageFile
from .class_素材文件夹结构 import ClassMaterialStructure
from .model import IMAGE_SUFFIX_LIST


class ClassGetAllEffectImage(ClassMaterialStructure):
    def __init__(self, root_path: Path) -> None:
        super().__init__(root_path)

    @property
    def all_effect_image(self) -> list[ClassEffectImageFile]:
        """
        所有效果图文件对象列表
        列表已按照文件stem中数字排序
        """
        return [
            ClassEffectImageFile(effect_image=obj, root_path=self.root_path)
            for obj in self.fun_遍历文件夹(
                in_path=self.effect_folder, suffix_list=IMAGE_SUFFIX_LIST
            )
        ]
