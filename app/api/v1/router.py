"""
v1 \u8def\u7531\u805a\u5408\u5165\u53e3\u3002\u65b0\u589e\u4e1a\u52a1\u8fd9\u91cc include_router \u5373\u53ef\u3002
"""

from fastapi import APIRouter

from app.api.v1.endpoints import agv, auth, task

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(agv.router, prefix="/agvs", tags=["agv"])
api_router.include_router(task.router, prefix="/tasks", tags=["task"])
