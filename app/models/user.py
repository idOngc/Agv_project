"""
\u7528\u6237 / \u89d2\u8272 \u6700\u7b80\u6a21\u578b\uff1aadmin / operator \u4e24\u79cd\u89d2\u8272\u3002

\u8868\u8bbe\u8ba1\u6545\u610f\u8bbe\u4e3a\u5e73\u9762\uff0c\u4e0d\u4e0a casbin / \u591a\u8868\u6743\u9650\uff0c\u540e\u671f\u6709\u9700\u8981\u518d\u6f14\u8fdb\u3002
"""

from enum import Enum

from tortoise import fields
from tortoise.models import Model


class Role(str, Enum):
    ADMIN = "admin"
    OPERATOR = "operator"


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=64, unique=True, description="\u767b\u5f55\u540d")
    password_hash = fields.CharField(max_length=255, description="bcrypt \u54c8\u5e0c")
    role = fields.CharEnumField(Role, default=Role.OPERATOR, description="\u89d2\u8272")
    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "user"

    def __str__(self) -> str:
        return f"<User {self.username} ({self.role})>"
