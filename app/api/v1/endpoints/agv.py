"""
AGV 资源 CRUD 占位。下一步补完。
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.agv import AGVCreateIn, AGVOut

router = APIRouter()


@router.get("", response_model=list[AGVOut], summary="列表 AGV (占位)")
async def list_agvs() -> list[AGVOut]:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO")


@router.post("", response_model=AGVOut, summary="新增 AGV (占位)")
async def create_agv(payload: AGVCreateIn) -> AGVOut:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO")
