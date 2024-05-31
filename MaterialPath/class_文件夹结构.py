from pathlib import Path


class MaterialFolderStructure:
    def __init__(self, root_folder: str) -> None:
        self.root_folder = Path(root_folder)

    @property
    def material_folder(self):
        return self.root_folder / self.root_folder.stem

    @property
    def effect_folder(self):
        return self.root_folder / "效果图"

    @property
    def preview_folder(self):
        return self.root_folder / "预览图"

    @property
    def web_folder(self):
        return self.root_folder / "WEB"
