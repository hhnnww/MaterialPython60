import shutil
from pathlib import Path

from PIL import Image

from class_material_path import ClassMaterialFile


class ClassCopyPreviewImageToPreviewPathImage(ClassMaterialFile):
    def __init__(self, material_file: Path, root_path: Path) -> None:
        super().__init__(material_file, root_path)

    def fun_复制到预览图(self):
        if self.preview_image.exists() is not True:
            return

        # 复制到预览图
        if self.preview_folder_image.parent.exists() is not True:
            self.preview_folder_image.parent.mkdir(parents=True)
        shutil.copyfile(self.preview_image, self.preview_folder_image)

        # 预览图拷贝到WEB图
        if self.web_folder_image.parent.exists() is not True:
            self.web_folder_image.parent.mkdir(parents=True)
        with Image.open(self.preview_folder_image.as_posix()) as im:
            im.thumbnail((500, 500))
            im.save(self.web_folder_image)
