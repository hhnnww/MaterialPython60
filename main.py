from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import router_基础信息.router
import router_获取信息.router
import router_获取图片.router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=router_获取信息.router.router, prefix="/material")
app.include_router(router=router_基础信息.router.router, prefix="/material")
app.include_router(router=router_获取图片.router.router, prefix="/material")
