from pathlib import Path

from pydantic import BaseModel

from MaterialPath.class_文件夹结构 import MaterialFolderStructure


class Model路径信息模型(BaseModel):
    stem: str
    path: str


class Model上下文件夹模型(BaseModel):
    current_path: Model路径信息模型
    prev_path: Model路径信息模型
    next_path: Model路径信息模型


class Class上下文件夹(MaterialFolderStructure):
    def __init__(self, root_folder: str) -> None:
        super().__init__(root_folder)

    @property
    def near_folder_model(self) -> Model上下文件夹模型:
        return Model上下文件夹模型(
            current_path=Model路径信息模型(
                stem=self.root_folder.stem, path=self.root_folder.as_posix()
            ),
            prev_path=Model路径信息模型(
                stem=self.prev_folder.stem, path=self.prev_folder.as_posix()
            ),
            next_path=Model路径信息模型(
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
