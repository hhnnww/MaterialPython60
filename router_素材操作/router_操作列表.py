from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ItemOut(BaseModel):
    action_list: list[list[str]]


@router.get("/get_actions")
def get_actions():
    return [
        ["移动到根目录", "文件重命名", "移动到数字目录", "复制到预览图", "删除广告文件"]
    ]
