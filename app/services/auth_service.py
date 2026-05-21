"""
认证业务层 —— 用户名 + 密码 验证 -> 颁发 JWT。

只做"账号是否能登录"这一件事,不做"账号管理"(增删用户走另外的服务)。
"""

from __future__ import annotations

from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.utils.exceptions import AppError


class InvalidCredentials(AppError):
    code = 1001
    msg = "用户名或密码错误"
    http_status = 401


class UserDisabled(AppError):
    code = 1002
    msg = "账号已被禁用"
    http_status = 403


async def authenticate(username: str, password: str) -> tuple[User, str]:
    """
    校验账号密码,成功返回 (User 实例, access_token)。
    任何失败统一抛 InvalidCredentials / UserDisabled,避免暴露具体原因。
    """
    user = await User.filter(username=username).first()
    if not user:
        # 这里故意不区分"用户不存在"和"密码错误",对抗用户名枚举
        raise InvalidCredentials()
    if not verify_password(password, user.password_hash):
        raise InvalidCredentials()
    if not user.is_active:
        raise UserDisabled()

    token = create_access_token(
        subject=user.id,
        extra={"username": user.username, "role": user.role.value},
    )
    return user, token
