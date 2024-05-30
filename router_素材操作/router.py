from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ItemIn(BaseModel):
    root_path: str
    shop_name: str

    path_start_stem: int
    file_start_stem: int


@router.post("/action")
def material_action(item_in: ItemIn):
    pass
