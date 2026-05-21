"""
FastAPI 依赖注入集中处。

- get_current_user:   解 JWT -> 返回当前 User 实例,鉴权失败抛 401
- require_admin:      在 get_current_user 之上检查角色为 admin,否则 403
"""

from __future__ import annotations

from fastapi import Header, HTTPException, status

from app.core.security import decode_access_token
from app.models.user import Role, User


async def get_current_user(authorization: str = Header(default="")) -> User:
    """
    从请求头 Authorization: Bearer <token> 中解 JWT,
    再去库里查出对应 User。任一环节失败一律 401。
    """
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "缺少 Bearer Token")
    token = authorization.split(" ", 1)[1].strip()

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token 无效或已过期")

    try:
        user_id = int(payload["sub"])
    except (TypeError, ValueError):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token 内容异常")

    user = await User.filter(id=user_id).first()
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "用户不存在")
    if not user.is_active:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "账号已被禁用")
    return user


async def require_admin(user: User = None) -> User:  # type: ignore[assignment]
    """
    管理员鉴权 —— 必须配合 get_current_user 一起 Depends。
    用法见 endpoints 里的示例。
    """
    # 注意:这个函数本身不直接拿 user,要靠下面那个组合依赖来拿
    raise RuntimeError("不要直接调用 require_admin,使用下面的 require_admin_dep")


from fastapi import Depends  # 放在文件下方避免循环 import 干扰


async def require_admin_dep(user: User = Depends(get_current_user)) -> User:
    """
    在 path operation 上 Depends(require_admin_dep) 就能拿到已校验为 admin 的 user。
    """
    if user.role != Role.ADMIN:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "需要 admin 权限")
    return user
