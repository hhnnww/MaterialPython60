from pydantic import BaseModel

from MaterialPath.class_1_素材文件夹 import MaterialFolder

from .class_上下文件夹 import Class上下文件夹


class Model素材格式信息(BaseModel):
    count: int
    count_title: str

    format: str
    format_title: str


class Class素材文件夹信息(MaterialFolder, Class上下文件夹):
    def __init__(self, root_folder: str) -> None:
        MaterialFolder.__init__(self, root_folder=root_folder)
        Class上下文件夹.__init__(self, root_folder=root_folder)

    @property
    def size_title(self) -> str:
        """235.32 GB"""
        size_level = ["b", "kb", "mb", "gb"]
        all_size = sum([obj.size for obj in self.all_material_obj])

        level = 0
        while all_size > 1000:
            all_size = all_size / 2014
            level += 1

        return f"{round(all_size,2)} {size_level[level].upper()}"

    @property
    def all_format(self) -> str:
        """ai"""
        return list(set([obj.format for obj in self.all_material_obj_sort_by_format]))[
            0
        ]

    @staticmethod
    def _get_format_title(format: str) -> str:
        match format:
            case ["psd", "psb"]:
                return "PSD 分层设计素材"
            case ["ai", "eps"]:
                return "AI 矢量设计素材"
            case ["ppt", "pptx"]:
                return "PPTX 幻灯片素材"
        return f"{format.upper()} 设计素材"

    def _get_count(self, format: str) -> int:
        """根据format输出数字"""
        return len([obj for obj in self.all_material_obj if obj.format == format])

    @property
    def comb_one_format(self) -> Model素材格式信息:
        """根据单个format组合对象"""
        return Model素材格式信息(
            count=self._get_count(format=self.all_format),
            count_title=f"{self._get_count(format=self.all_format)} 个{self.all_format.upper()} 文件",
            format=self.all_format.upper(),
            format_title=self._get_format_title(format=self.all_format),
        )
