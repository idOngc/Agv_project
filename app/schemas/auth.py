"""登录相关 schema。"""

from pydantic import BaseModel


class LoginIn(BaseModel):
    username: str
    password: str


class UserBrief(BaseModel):
    """登录成功后回传给前端的用户精简信息。"""
    id: int
    username: str
    role: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserBrief
