from pathlib import Path


class Class素材文件夹结构:
    def __init__(self, root_folder: str) -> None:
        self.root_folder = Path(root_folder)

    @property
    def fun_源文件文件夹(self):
        return self.root_folder / self.root_folder.stem

    @property
    def fun_效果图文件夹(self):
        return self.root_folder / "效果图"

    @property
    def fun_预览图文件夹(self):
        return self.root_folder / "预览图"

    @property
    def fun_web文件夹(self):
        return self.root_folder / "WEB"
