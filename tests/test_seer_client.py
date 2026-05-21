"""
SEER 客户端集成测试 —— 起一个本地 fake AGV TCP server, 测请求/响应配对。

这个测试不依赖真实 AGV,可以放在 CI 跑。
"""

from __future__ import annotations

import asyncio

import pytest

from app.connectors.seer.client import (
    SeerNotConnected,
    SeerRequestTimeout,
    SeerTcpClient,
)
from app.connectors.seer.protocol import HEADER_SIZE, AGVProtocol


class FakeSeerServer:
    """模拟一台仙工 AGV:收到请求就用相同 req_id 回一个固定 body。"""

    def __init__(self, reply_body: dict, *, delay: float = 0.0, drop: bool = False):
        self.reply_body = reply_body
        self.delay = delay
        self.drop = drop
        self.server: asyncio.AbstractServer | None = None
        self.port: int = 0
        self.received: list[tuple[int, int, dict]] = []

    async def start(self) -> None:
        self.server = await asyncio.start_server(self._handle, "127.0.0.1", 0)
        self.port = self.server.sockets[0].getsockname()[1]

    async def stop(self) -> None:
        if self.server is not None:
            self.server.close()
            await self.server.wait_closed()

    async def _handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        buf = b""
        try:
            while not reader.at_eof():
                chunk = await reader.read(4096)
                if not chunk:
                    return
                buf += chunk
                pkts, buf = AGVProtocol.unpack(buf)
                for req_id, msg_type, body, _ in pkts:
                    self.received.append((req_id, msg_type, body))
                    if self.drop:
                        continue
                    if self.delay:
                        await asyncio.sleep(self.delay)
                    raw = AGVProtocol.pack(req_id, msg_type, self.reply_body)
                    writer.write(raw)
                    await writer.drain()
        except (ConnectionResetError, asyncio.CancelledError):
            pass


@pytest.mark.asyncio
async def test_send_request_roundtrip():
    srv = FakeSeerServer({"model": "fake", "sn": "X-001"})
    await srv.start()
    try:
        client = SeerTcpClient("fake-agv", "127.0.0.1", srv.port, connect_timeout=1.0)
        resp = await client.send_request(1000, None, timeout=2.0)
        assert resp.msg_type == 1000
        assert resp.body == {"model": "fake", "sn": "X-001"}
        assert len(srv.received) == 1
        await client.close()
    finally:
        await srv.stop()


@pytest.mark.asyncio
async def test_concurrent_requests_keep_req_id_distinct():
    """并发 20 个请求, 每个 req_id 互不冲突, 全部能拿到自己的响应。"""
    srv = FakeSeerServer({"ack": True})
    await srv.start()
    try:
        client = SeerTcpClient("fake-agv", "127.0.0.1", srv.port, connect_timeout=1.0)
        results = await asyncio.gather(
            *(client.send_request(1000, {"i": i}, timeout=2.0) for i in range(20))
        )
        assert len(results) == 20
        assert {r.req_id for r in results} == {r.req_id for r in results}  # 全去重也只有 20 个
        assert len({r.req_id for r in results}) == 20
        await client.close()
    finally:
        await srv.stop()


@pytest.mark.asyncio
async def test_request_timeout_when_server_drops():
    """server 收了但不回,client 应抛 SeerRequestTimeout。"""
    srv = FakeSeerServer({}, drop=True)
    await srv.start()
    try:
        client = SeerTcpClient("fake-agv", "127.0.0.1", srv.port, connect_timeout=1.0)
        with pytest.raises(SeerRequestTimeout):
            await client.send_request(1000, None, timeout=0.5)
        await client.close()
    finally:
        await srv.stop()


@pytest.mark.asyncio
async def test_connect_unreachable_raises():
    """连一个不存在的端口直接抛 SeerNotConnected。"""
    client = SeerTcpClient("nowhere", "127.0.0.1", 1, connect_timeout=0.5)
    with pytest.raises(SeerNotConnected):
        await client.send_request(1000, None, timeout=1.0)
    await client.close()
