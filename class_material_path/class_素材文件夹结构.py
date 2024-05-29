from pathlib import Path


class ClassMaterialStructure:
    """素材文件夹结构组建"""

    def __init__(self, root_path: Path) -> None:
        self.root_path = root_path

    @property
    def material_folder(self) -> Path:
        """素材目录"""
        return self.root_path / self.root_path.stem

    @property
    def preview_folder(self) -> Path:
        """预览图目录"""
        return self.root_path / "预览图"

    @property
    def effect_folder(self) -> Path:
        """效果图目录"""
        return self.root_path / "效果图"

    @property
    def web_folder(self) -> Path:
        """WEB图片目录"""
        return self.root_path / "WEB"
