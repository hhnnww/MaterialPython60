from pathlib import Path

from class_material_path.class_素材文件 import ClassMaterialFile


class ClassMoveToNumPath(ClassMaterialFile):
    def __init__(self, material_file: Path, root_path: Path) -> None:
        super().__init__(material_file, root_path)

    @property
    def _center_stem(self) -> str:
        start_num = str(int(self.num / 100) * 100)
        end_num = str((int(self.num / 100) * 100) + 99)

        return f"{start_num}-{end_num}"

    def fun_移动到数字目录(self):
        self.material_file.rename(
            self.material_folder / self._center_stem / self.material_file.name
        )

        if self.preview_image.exists():
            self.preview_image.rename(
                self.material_folder / self._center_stem / self.preview_image.name
            )

        if self.preview_folder_image.exists():
            self.preview_folder_image.rename(
                self.preview_folder / self._center_stem / self.preview_folder_image.name
            )

        if self.web_folder_image.exists():
            self.web_folder_image.rename(
                self.web_folder / self._center_stem / self.web_folder_image.name
            )
