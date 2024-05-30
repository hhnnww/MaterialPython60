from pathlib import Path

from .class_素材文件夹结构 import ClassMaterialStructure


class ClassPrevNextMaterialPath(ClassMaterialStructure):
    def __init__(self, root_path: Path) -> None:
        super().__init__(root_path)

    @property
    def _num_str(self) -> str:
        return self.root_path.stem[1:]

    @property
    def _num(self) -> int:
        return int(self._num_str)

    @property
    def prev_path(self) -> Path:
        stem = f"{self.root_path.stem[0]}{str(self._num-1).zfill(len(self._num_str))}"
        return self.root_path.parent / stem

    @property
    def next_path(self) -> Path:
        stem = f"{self.root_path.stem[0]}{str(self._num+1).zfill(len(self._num_str))}"
        return self.root_path.parent / stem
