"""
\u4ed9\u5de5 AGV \u9ad8\u5c42\u8bed\u4e49\u5c01\u88c5 \u2014\u2014 \u4e0b\u4e00\u6b65\u5b9e\u73b0\u3002

\u8fd9\u4e2a\u6587\u4ef6\u662f\u300c\u8fde\u63a5\u5c42\u5bf9\u4e0a\u66b4\u9732\u7684\u552f\u4e00\u51fa\u53e3\u300d\u3002\u4e0a\u5c42 (services) \u53ea\u8c03 SeerAPI\uff0c
\u4e0d\u8c03 SeerTcpClient\u3002

\u4f8b\u5982:
    class SeerAPI(AGVConnector):
        async def navigate(self, target_point: str) -> dict[str, Any]:
            return (await self._nav.send_request(
                NavMsgType.NAVIGATE_TO_POINT,
                {"task_id": str(uuid4()), "id": target_point},
            )).body
"""

# from __future__ import annotations
# from typing import Any
# from app.connectors.base import AGVConnector
# from app.connectors.seer.client import SeerTcpClient
#
# class SeerAPI(AGVConnector):
#     def __init__(self, agv_name: str, ip: str): ...
#     async def navigate(self, target_point: str, **kw: Any) -> dict[str, Any]: ...
#     async def cancel_task(self) -> dict[str, Any]: ...
#     async def get_status(self) -> dict[str, Any]: ...
