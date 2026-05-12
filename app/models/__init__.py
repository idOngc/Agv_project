"""
\u663e\u793a\u5bfc\u51fa\u6240\u6709\u6a21\u578b\uff0c\u65b9\u4fbf\u522b\u5904 `from app.models import AGV, Task` \u4f7f\u7528\u3002

\u6ce8\u610f\uff1aAerich \u662f\u901a\u8fc7\u8bfb\u53d6 `tortoise_conf.TORTOISE_ORM` \u91cc\u7684\u6a21\u5757\u8def\u5f84\u53d1\u73b0\u6a21\u578b\u7684\uff0c
      \u4e0d\u662f\u8bfb\u8fd9\u91cc\uff0c\u6240\u4ee5\u65b0\u589e\u8868\u8bb0\u5f97\u540c\u6b65\u53bb tortoise_conf.py \u52a0\u8def\u5f84\u3002
"""

from app.models.agv import AGV
from app.models.task import Task
from app.models.user import Role, User

__all__ = ["User", "Role", "AGV", "Task"]
