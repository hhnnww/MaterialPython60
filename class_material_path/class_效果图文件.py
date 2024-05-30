from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .class_素材文件夹结构 import ClassMaterialStructure
from .fun_获取数字 import fun_获取数字


class ModelEffectImage(BaseModel):
    effect_image: str
    web_image: Optional[str] = None


class ClassEffectImageFile(ClassMaterialStructure):
    def __init__(
        self,
        effect_image: Path,
        root_path: Path,
    ) -> None:
        self.effect_image = effect_image
        super().__init__(root_path=root_path)

    @property
    def model(self) -> ModelEffectImage:
        obj = ModelEffectImage(effect_image=self.effect_image.as_posix())
        if self.web_image.exists():
            obj.web_image = self.web_image.as_posix()
        return obj

    @property
    def web_image(self) -> Path:
        return Path(
            self.effect_image.as_posix().replace(
                self.effect_folder.as_posix(), self.web_folder.as_posix()
            )
        )

    @property
    def num(self) -> int:
        return fun_获取数字(self.effect_image.stem)
