from pathlib import Path


def fun_root_init(root_path: Path):
    if len(root_path.parts) <= 3:
        raise IndexError("文件夹路径太短")

    if root_path.is_absolute() is not True:
        raise IndexError("必须为绝对路径")

    if root_path.stem == root_path.parent.stem:
        raise IndexError("不能和父路径同名")

    if "-" in root_path.stem:
        raise IndexError("路径不能包含符号 -")
