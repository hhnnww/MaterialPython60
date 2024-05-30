from fastapi import FastAPI

import router_素材信息
import router_素材操作

app = FastAPI()

app.include_router(router=router_素材信息.router, prefix="/material_info")
app.include_router(router=router_素材操作.router, prefix="/material_action")
