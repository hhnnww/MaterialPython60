from tqdm import tqdm

from class_material_path import ClassMaterialPath

from .class_素材文件操作 import ClassMaterialFileAction


class ClassMaterialAction(ClassMaterialPath):
    def __init__(self, root_path: str, shop_name: str) -> None:
        super().__init__(root_path=root_path)
        self.shop_name = shop_name

    @property
    def all_material_file_with_action(self) -> tqdm[ClassMaterialFileAction]:
        """包含素材文件操作的类的素材文件列表"""
        return tqdm(
            [
                ClassMaterialFileAction(
                    material_file=obj.material_file,
                    root_path=self.root_path,
                    shop_name=self.shop_name,
                )
                for obj in self.all_material_file
            ],
            ncols=100,
        )
