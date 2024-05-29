from pathlib import Path

from .class_素材文件夹结构 import ClassMaterialStructure
from .class_获取所有效果图图片 import ClassGetAllEffectImage
from .class_获取所有素材文件 import ClassGetAllMaterialFile


class ClassMaterialPath(
    ClassMaterialStructure, ClassGetAllMaterialFile, ClassGetAllEffectImage
):
    def __init__(self, root_path: str) -> None:
        self.root_path = Path(root_path)
        ClassMaterialStructure.__init__(self, root_path=self.root_path)
        ClassGetAllMaterialFile.__init__(
            self,
            material_folder=self.material_folder,
            preview_folder=self.preview_folder,
            web_folder=self.web_folder,
        )
        ClassGetAllEffectImage.__init__(
            self, effect_folder=self.effect_folder, web_folder=self.web_folder
        )


if __name__ == "__main__":
    cla = ClassMaterialPath(root_path="")
    print(cla.all_effect_image)
