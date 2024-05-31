from pathlib import Path

from pydantic import BaseModel

from .class_文件夹结构 import MaterialFolderStructure
from .class_素材文件信息 import MateiralFileInfo


class ModelFile(BaseModel):
    path: str
    exists: bool


class ModelMaterialFile(BaseModel):
    material_file: str
    preview_image: ModelFile
    preview_folder_image: ModelFile
    web_folder_image: ModelFile


class MaterialFile(MaterialFolderStructure, MateiralFileInfo):
    def __init__(self, material_file: Path, root_folder: str) -> None:
        MaterialFolderStructure.__init__(self, root_folder=root_folder)
        MateiralFileInfo.__init__(self, material_file=material_file)

    @property
    def model(self):
        return ModelMaterialFile(
            material_file=self.material_file.as_posix(),
            preview_image=ModelFile(
                path=self.preview_image.as_posix(), exists=self.preview_image.exists()
            ),
            preview_folder_image=ModelFile(
                path=self.preview_folder_image.as_posix(),
                exists=self.preview_folder_image.exists(),
            ),
            web_folder_image=ModelFile(
                path=self.web_folder_image.as_posix(),
                exists=self.web_folder_image.exists(),
            ),
        )

    @property
    def preview_image(self):
        png_path = self.material_file.with_suffix(".png")
        return png_path

    @property
    def preview_folder_image(self):
        return Path(
            self.preview_image.as_posix().replace(
                self.material_folder.as_posix(), self.preview_folder.as_posix()
            )
        )

    @property
    def web_folder_image(self):
        return Path(
            self.preview_folder_image.as_posix().replace(
                self.root_folder.as_posix(), self.web_folder.as_posix()
            )
        )
