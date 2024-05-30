from pathlib import Path

from .class_上下文件夹 import ClassPrevNextMaterialPath
from .class_素材文件夹结构 import ClassMaterialStructure
from .class_获取所有效果图图片 import ClassGetAllEffectImage
from .class_获取所有素材文件 import ClassGetAllMaterialFile
from .fun_root_path初始化 import fun_root_init


class ClassMaterialPath(
    ClassGetAllMaterialFile,
    ClassGetAllEffectImage,
    ClassPrevNextMaterialPath,
    ClassMaterialStructure,
):
    """构建素材文件夹对象

    Args:
        ClassGetAllMaterialFile (_type_): 所有素材文件
        ClassGetAllEffectImage (_type_): 所有效果图文件
        ClassPrevNextMaterialPath (_type_): 上下文件夹
        ClassMaterialStructure (_type_): 文件夹结构
    """

    def __init__(self, root_path: str) -> None:
        self.root_path = Path(root_path)
        fun_root_init(self.root_path)

        ClassMaterialStructure.__init__(self, root_path=self.root_path)
        ClassGetAllMaterialFile.__init__(self, root_path=self.root_path)
        ClassGetAllEffectImage.__init__(self, root_path=self.root_path)
        ClassPrevNextMaterialPath.__init__(self, root_path=self.root_path)
