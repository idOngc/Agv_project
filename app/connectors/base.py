"""
\u8fde\u63a5\u5668\u62bd\u8c61\u57fa\u7c7b \u2014\u2014 \u4e3a\u540e\u7eed\u591a\u53a8\u5546(\u4ed9\u5de5 / \u5176\u5b83) \u7edf\u4e00\u63a5\u53e3\u3002

\u53ea\u5b9a\u4e49\u8bed\u4e49\u5c42\u65b9\u6cd5\u540d\uff0c\u4e0d\u5173\u5fc3\u5b9e\u73b0\u3002\u4e0a\u5c42\u5bf9\u63a5\u8fd9\u4e2a\u62bd\u8c61\uff0c\u4e0d\u5bf9\u63a5\u5b50\u7c7b\u3002
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AGVConnector(ABC):
    """\u4efb\u610f AGV \u53a8\u5546\u8fde\u63a5\u5668\u7684\u62bd\u8c61\u63a5\u53e3\u3002"""

    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    async def is_alive(self) -> bool: ...

    @abstractmethod
    async def navigate(self, target_point: str, **kwargs: Any) -> dict[str, Any]:
        """\u4e0b\u53d1\u5bfc\u822a\u4efb\u52a1\uff0c\u8fd4\u56de AGV \u54cd\u5e94 body\u3002"""

    @abstractmethod
    async def cancel_task(self) -> dict[str, Any]:
        """\u53d6\u6d88\u5f53\u524d\u4efb\u52a1\u3002"""

    @abstractmethod
    async def get_status(self) -> dict[str, Any]:
        """\u67e5\u8be2\u72b6\u6001\u5feb\u7167\u3002"""
