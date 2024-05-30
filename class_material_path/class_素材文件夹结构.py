from pathlib import Path

from .fun_获取数字 import fun_获取数字


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

    @staticmethod
    def fun_遍历文件夹(in_path: Path, suffix_list: list[str]) -> list[Path]:
        file_list: list[Path] = []
        for in_file in in_path.rglob("*"):
            if in_file.is_file() and in_file.suffix.lower() in suffix_list:
                file_list.append(in_file)

        file_list.sort(key=lambda k: fun_获取数字(k.stem))
        return file_list
