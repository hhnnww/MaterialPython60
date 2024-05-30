from tqdm import tqdm

from class_material_path import ClassMaterialPath

from .class_素材文件操作 import ClassMaterialFileAction


class ClassMaterialFolderAction(ClassMaterialPath):
    def __init__(self, root_path: str, action: str) -> None:
        super().__init__(root_path=root_path)
        self.action = action

    @property
    def all_material_file_with_action(self) -> tqdm[ClassMaterialFileAction]:
        """包含素材文件操作的类的素材文件列表"""
        return tqdm(
            [
                ClassMaterialFileAction(
                    material_file=obj.material_file,
                    root_path=self.root_path,
                )
                for obj in self.all_material_file
            ],
            ncols=100,
            desc=f"{self.action}",
        )
