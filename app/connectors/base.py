"""
连接器抽象基类 —— 为后续多厨商(仙工 / 其它) 统一接口。

只定义语义层方法名，不关心实现。上层对接这个抽象，不对接子类。
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AGVConnector(ABC):
    """任意 AGV 厨商连接器的抽象接口。"""

    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    async def is_alive(self) -> bool: ...

    @abstractmethod
    async def navigate(self, target_point: str, **kwargs: Any) -> dict[str, Any]:
        """下发导航任务，返回 AGV 响应 body。"""

    @abstractmethod
    async def cancel_task(self) -> dict[str, Any]:
        """取消当前任务。"""

    @abstractmethod
    async def get_status(self) -> dict[str, Any]:
        """查询状态快照。"""
