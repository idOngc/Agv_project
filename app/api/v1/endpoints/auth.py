"""
\u767b\u5f55 / \u5237\u65b0\u63a5\u53e3\u5360\u4f4d\u3002\u540e\u7eed\u63a5\u5165 User \u8868\u540e\u8865\u5b8c\u3002
"""

from fastapi import APIRouter, HTTPException, status

from app.core.security import create_access_token, verify_password
from app.schemas.auth import LoginIn, TokenOut

router = APIRouter()


@router.post("/login", response_model=TokenOut, summary="\u767b\u5f55\u83b7\u53d6 JWT (\u5360\u4f4d)")
async def login(payload: LoginIn) -> TokenOut:
    # TODO: \u4ece User \u8868\u67e5\u8bc1 + verify_password
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "auth/login \u5f85\u63a5\u5165 User \u8868\u540e\u5b9e\u73b0")
