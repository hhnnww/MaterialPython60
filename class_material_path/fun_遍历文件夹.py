from pathlib import Path

from .fun_获取数字 import fun_获取数字


def fun_遍历文件夹(in_path: Path, suffix_list: list[str]) -> list[Path]:
    file_list: list[Path] = []
    for in_file in in_path.rglob("*"):
        if in_file.is_file() and in_file.suffix.lower() in suffix_list:
            file_list.append(in_file)

    file_list.sort(key=lambda k: fun_获取数字(k.stem))
    return file_list
