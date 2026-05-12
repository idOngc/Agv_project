"""
FastAPI \u4f9d\u8d56\u6ce8\u5165\u96c6\u4e2d\u5904\u3002\u73b0\u5728\u5148\u653e\u5360\u4f4d\uff0c\u540e\u7eed\u6dfb\u52a0:
  - get_current_user
  - require_admin
  - get_agv_manager
"""

from fastapi import Header, HTTPException, status

from app.core.security import decode_access_token


async def get_current_user_sub(authorization: str = Header(default="")) -> str:
    """
    \u6700\u7b80\u5b9e\u73b0\uff1a\u4ec5\u4ece Authorization: Bearer <token> \u91cc\u62cd payload \u7684 sub\u3002
    \u540e\u7eed\u63a5\u5165 User \u8868\u540e\u8fd9\u91cc\u8fd4\u56de User \u5b9e\u4f8b\u3002
    """
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Missing bearer token")
    token = authorization.split(" ", 1)[1].strip()
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
    return payload["sub"]
