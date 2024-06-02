import re
from pathlib import Path


class Class公共功能:
    @staticmethod
    def fun_获取数字(stem: str) -> int:
        num_list = re.findall(r"\d+", stem)
        if len(num_list) == 0:
            return 0

        return int("".join(num_list))

    def fun_遍历文件夹(self, folder: Path, suffix_list: list[str]) -> list[Path]:
        ma_list = [
            in_file
            for in_file in folder.rglob("*")
            if in_file.is_file() and in_file.suffix.lower() in suffix_list
        ]
        ma_list.sort(key=lambda k: self.fun_获取数字(k.stem))
        return ma_list

    material_suffix_list = [".ai", ".eps", ".psd", ".psb", ".ppt", ".pptx"]
    image_suffix_list = [".gif", ".jpg", ".jpeg", ".png"]
    ad_suffix_list = [".txt", ".html", ".htm", ".link"]
