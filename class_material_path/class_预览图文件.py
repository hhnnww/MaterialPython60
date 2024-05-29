from pathlib import Path


class ClassPreviewImage:
    def __init__(
        self,
        preview_image: Path,
        material_folder: Path,
        preview_folder: Path,
        web_folder: Path,
    ) -> None:
        self.preview_image = preview_image

        self.material_folder = material_folder
        self.preview_folder = preview_folder
        self.web_folder = web_folder

    @property
    def preview_folder_image(self) -> Path:
        """预览图文件夹中的预览图"""
        return Path(
            self.preview_image.as_posix().replace(
                self.material_folder.as_posix(), self.preview_folder.as_posix()
            )
        )

    @property
    def web_folder_image(self) -> Path:
        """web文件夹中的预览图"""
        return Path(
            self.preview_folder_image.as_posix().replace(
                self.preview_folder.as_posix(), self.web_folder.as_posix()
            )
        )
