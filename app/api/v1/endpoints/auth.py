"""
登录 / 刷新接口占位。后续接入 User 表后补完。
"""

from fastapi import APIRouter, HTTPException, status

from app.core.security import create_access_token, verify_password
from app.schemas.auth import LoginIn, TokenOut

router = APIRouter()


@router.post("/login", response_model=TokenOut, summary="登录获取 JWT (占位)")
async def login(payload: LoginIn) -> TokenOut:
    # TODO: 从 User 表查证 + verify_password
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "auth/login 待接入 User 表后实现")
