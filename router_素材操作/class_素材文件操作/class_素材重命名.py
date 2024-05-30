from pathlib import Path

from class_material_path.class_素材文件 import ClassMaterialFile


class ClassMatrialFileRename(ClassMaterialFile):
    def __init__(
        self,
        material_file: Path,
        root_path: Path,
    ) -> None:
        super().__init__(material_file, root_path)

    def fun_素材重命名(self, new_stem: str):
        self.material_file.rename(self.material_file.with_stem(new_stem))

        if self.preview_image.exists():
            self.preview_image.rename(self.preview_image.with_stem(new_stem))

        if self.preview_folder_image.exists():
            self.preview_folder_image.rename(
                self.preview_folder_image.with_stem(new_stem)
            )

        if self.web_folder_image.exists():
            self.web_folder_image.rename(self.preview_folder_image.with_stem(new_stem))
