from pathlib import Path

from class_material_path.class_素材文件 import ClassMaterialFile


class ClassMaterialFileMoveRootFolder(ClassMaterialFile):
    def __init__(self, material_file: Path, root_path: Path) -> None:
        super().__init__(material_file, root_path)

    def fun_移动到根目录(self):
        if self.material_file.parent != self.material_folder:
            self.material_file.rename(self.material_folder / self.material_file.name)

            if self.preview_image.exists():
                self.preview_image.rename(
                    self.material_folder / self.preview_image.name
                )

            if self.preview_folder_image.exists():
                self.preview_folder_image.rename(
                    self.preview_folder / self.preview_folder_image.name
                )

            if self.web_folder_image.exists():
                self.web_folder_image.rename(
                    self.web_folder / self.web_folder_image.name
                )
