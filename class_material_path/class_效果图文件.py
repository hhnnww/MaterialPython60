from pathlib import Path

from .fun_获取数字 import fun_获取数字


class ClassEffectImageFile:
    def __init__(
        self, effect_image: Path, effect_folder: Path, web_folder: Path
    ) -> None:
        self.effect_image = effect_image
        self.effect_folder = effect_folder
        self.web_folder = web_folder

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
