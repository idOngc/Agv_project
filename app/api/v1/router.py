"""
v1 路由聚合入口。新增业务这里 include_router 即可。
"""

from fastapi import APIRouter

from app.api.v1.endpoints import agv, auth, task

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(agv.router, prefix="/agvs", tags=["agv"])
api_router.include_router(task.router, prefix="/tasks", tags=["task"])
