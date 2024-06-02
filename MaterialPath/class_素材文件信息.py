from pathlib import Path

from .class_共用功能 import BaseFunction


class MateiralFileInfo(BaseFunction):
    def __init__(self, material_file: Path) -> None:
        self.material_file = material_file
        super().__init__()

    @property
    def format(self) -> str:
        format = self.material_file.suffix.lower().replace(".", "")
        match format:
            case "psb" | "psd":
                return "psd"

            case "eps" | "ai":
                return "ai"

            case "ppt" | "pptx":
                return "pptx"

        return format

    @property
    def size(self) -> int:
        return self.material_file.stat().st_size

    @property
    def num(self) -> int:
        return self.fun_获取数字(self.material_file.stem)

    @property
    def format_level(self) -> int:
        match self.format:
            case "ai":
                return 0

            case "psd":
                return 1

            case "pptx":
                return 2

        return 9
