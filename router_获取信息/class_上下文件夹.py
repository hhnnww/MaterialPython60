from pathlib import Path

from pydantic import BaseModel

from MaterialPath.class_文件夹结构 import MaterialFolderStructure


class ModelPathItem(BaseModel):
    stem: str
    path: str


class ModelPrevAndNext(BaseModel):
    prev_path: ModelPathItem
    next_path: ModelPathItem


class PrevNextPath(MaterialFolderStructure):
    def __init__(self, root_folder: str) -> None:
        super().__init__(root_folder)

    @property
    def near_folder_model(self) -> ModelPrevAndNext:
        return ModelPrevAndNext(
            prev_path=ModelPathItem(
                stem=self.prev_folder.stem, path=self.prev_folder.as_posix()
            ),
            next_path=ModelPathItem(
                stem=self.next_folder.stem, path=self.next_folder.as_posix()
            ),
        )

    @property
    def _current_num(self) -> int:
        try:
            num = int(self.root_folder.stem[1:])
        except ValueError:
            return 2
        else:
            return num

    @property
    def prev_folder(self) -> Path:
        return (
            self.root_folder.parent
            / f"{self.root_folder.stem[0]}{str(self._current_num-1).rjust(len(self.root_folder.stem)-1,'0')}"
        )

    @property
    def next_folder(self) -> Path:
        return (
            self.root_folder.parent
            / f"{self.root_folder.stem[0]}{str(self._current_num+1).rjust(len(self.root_folder.stem)-1,'0')}"
        )
