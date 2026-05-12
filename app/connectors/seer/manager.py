"""
\u591a\u53f0 AGV \u8fde\u63a5\u6c60 / \u5168\u5c40\u5355\u4f8b \u2014\u2014 \u4e0b\u4e00\u6b65\u5b9e\u73b0\u3002

\u804c\u8d23:
  - \u542f\u52a8\u65f6\u4ece\u6570\u636e\u5e93\u52a0\u8f7d\u6240\u6709 is_active=True \u7684 AGV\uff0c\u6309\u7167 ip:port \u5e76\u53d1\u8fde\u63a5
  - \u4e0a\u5c42 service \u901a\u8fc7 get(agv_uuid) -> SeerAPI \u62ff\u5230\u8fde\u63a5\u53e5\u67c4
  - close_all() \u5728 lifespan shutdown \u65f6\u88ab\u8c03
  - \u70ed\u589e/\u70ed\u5220 (AGV \u88ab\u542f\u7528/\u7981\u7528\u65f6\u540c\u6b65\u52a0\u5165/\u9000\u51fa\u8fde\u63a5\u6c60)
"""

# from __future__ import annotations
# from app.connectors.seer.api import SeerAPI
#
# class SeerManager:
#     def __init__(self): self._pool: dict[str, SeerAPI] = {}
#     async def init_from_db(self) -> None: ...
#     def get(self, agv_uuid: str) -> SeerAPI: ...
#     async def close_all(self) -> None: ...
#
# seer_manager = SeerManager()  # \u5168\u5c40\u5355\u4f8b
