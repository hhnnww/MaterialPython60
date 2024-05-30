from fastapi import FastAPI

from router_素材信息 import router

app = FastAPI()

app.include_router(router, prefix="/material_info")
