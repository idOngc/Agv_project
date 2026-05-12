"""
AGV \u8d44\u6e90 CRUD \u5360\u4f4d\u3002\u4e0b\u4e00\u6b65\u8865\u5b8c\u3002
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.agv import AGVCreateIn, AGVOut

router = APIRouter()


@router.get("", response_model=list[AGVOut], summary="\u5217\u8868 AGV (\u5360\u4f4d)")
async def list_agvs() -> list[AGVOut]:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO")


@router.post("", response_model=AGVOut, summary="\u65b0\u589e AGV (\u5360\u4f4d)")
async def create_agv(payload: AGVCreateIn) -> AGVOut:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO")
