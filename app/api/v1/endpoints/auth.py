"""
登录接口。

- POST /api/v1/auth/login   用户名密码换 JWT
- GET  /api/v1/auth/me      返回当前登录用户信息(需 Bearer Token)
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.auth import LoginIn, TokenOut, UserBrief
from app.services.auth_service import authenticate

router = APIRouter()


@router.post("/login", response_model=TokenOut, summary="登录获取 JWT")
async def login(payload: LoginIn) -> TokenOut:
    user, token = await authenticate(payload.username, payload.password)
    return TokenOut(
        access_token=token,
        user=UserBrief(id=user.id, username=user.username, role=user.role.value),
    )


@router.get("/me", response_model=UserBrief, summary="当前登录用户")
async def me(user: User = Depends(get_current_user)) -> UserBrief:
    return UserBrief(id=user.id, username=user.username, role=user.role.value)
