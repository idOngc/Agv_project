"""
仙工 (SEER) AGV 连接子包。

文件职责:
  - protocol.py    二进制报文打包 / 解包 (纯函数)
  - constants.py   端口表 + msg_type 按能力分类
  - client.py      单台 AGV 的 asyncio TCP 长连接 (占位)
  - api.py         navigate/get_status/cancel 等高层语义封装 (占位)
  - manager.py     多台 AGV 连接池 / 全局单例 (占位)
"""
