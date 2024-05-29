import re


def fun_获取数字(stem: str) -> int:
    num_list = re.findall(r"\d+", stem)
    if len(num_list) == 0:
        return 0

    return int("".join(num_list))
