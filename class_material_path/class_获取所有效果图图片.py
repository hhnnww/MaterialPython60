from pathlib import Path

from class_material_path.model import IMAGE_SUFFIX_LIST

from .class_效果图文件 import ClassEffectImageFile


class ClassGetAllEffectImage:
    def __init__(self, effect_folder: Path, web_folder: Path) -> None:
        self.effect_folder = effect_folder
        self.web_folder = web_folder

    @property
    def all_effect_image(self) -> list[ClassEffectImageFile]:
        """
        所有效果图文件对象列表
        列表已按照文件stem中数字排序
        """
        effect_image_list: list[ClassEffectImageFile] = []
        for in_file in self.effect_folder.rglob("*"):
            if in_file.is_file() and in_file.suffix.lower() in IMAGE_SUFFIX_LIST:
                effect_image_list.append(
                    ClassEffectImageFile(
                        effect_image=in_file,
                        effect_folder=self.effect_folder,
                        web_folder=self.web_folder,
                    )
                )

        effect_image_list.sort(key=lambda k: k.num)
        return effect_image_list
