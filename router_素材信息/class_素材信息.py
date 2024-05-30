from typing import List

from pydantic import BaseModel

from class_material_path import ClassMaterialPath


class ModelMateiralItemFormat(BaseModel):
    """单个素材后缀信息
    'AI','AI 矢量设计素材','28','28个 AI 文件'
    """

    format: str
    format_title: str
    count: int
    count_title: str


class ClassMaterialInfo(ClassMaterialPath):
    def __init__(self, root_path: str) -> None:
        super().__init__(root_path=root_path)

    @property
    def _all_format(self) -> List[str]:
        """获取一个素材文件夹中的所有格式"""
        return list(set([obj.format.lower() for obj in self.all_material_file]))

    def _comb_one_suffix(self, format: str) -> ModelMateiralItemFormat:
        """根据单个格式,获取格式标题,格式数量,数量标题"""
        count = len(
            [obj.format for obj in self.all_material_file if obj.format == format]
        )
        return ModelMateiralItemFormat(
            format=format.upper(),
            format_title=self._format_title(format=format),
            count=count,
            count_title=f"{count} 个 {format.upper()} 文件",
        )

    @staticmethod
    def _format_title(format: str):
        """根据的单个格式获取格式标题"""
        match format:
            case ["ai", "eps"]:
                return "AI 矢量设计素材"

            case ["psd", "psb"]:
                return "PSD 设计素材"

            case ["ppt", "pptx"]:
                return "PPT 幻灯片素材"

        return f"{format.upper()} 设计素材"

    @property
    def size(self) -> str:
        """获取所有尺寸,然后输出尺寸标题"""
        size_level = ["b", "kb", "mb", "gb"]
        all_size = sum([obj.size for obj in self.all_material_file])
        level = 0

        while all_size > 1000:
            all_size = all_size / 1024
            level += 1

        return f"{round(all_size,2)} {size_level[level].upper()}"

    @property
    def all_format_item(self) -> list[ModelMateiralItemFormat]:
        """构建所有格式模型,遍历所有格式,然后根据格式输出模型"""
        format_item_list = []
        for obj in self._all_format:
            format_item_list.append(self._comb_one_suffix(format=obj))
        return format_item_list
