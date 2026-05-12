"""
\u534f\u8bae\u5c42\u5355\u6d4b \u2014\u2014 \u53ea\u9a8c pack/unpack \u5728\u5404\u79cd\u7c98\u5305 / \u9519\u8bef\u5bf9\u9f50\u573a\u666f\u4e0b\u7684\u8868\u73b0\u3002
"""

from app.connectors.seer.protocol import (
    HEADER_SIZE,
    MAX_BODY_LEN,
    START_BYTE,
    AGVProtocol,
)


def test_pack_and_unpack_roundtrip():
    body = {"hello": "world", "n": 42}
    packed = AGVProtocol.pack(req_id=1, msg_type=1001, body=body)

    packets, remaining = AGVProtocol.unpack(packed)
    assert remaining == b""
    assert len(packets) == 1
    req_id, msg_type, body_dict, raw = packets[0]
    assert req_id == 1
    assert msg_type == 1001
    assert body_dict == body
    assert raw == packed


def test_pack_empty_body():
    packed = AGVProtocol.pack(req_id=7, msg_type=1, body=None)
    assert len(packed) == HEADER_SIZE
    packets, remaining = AGVProtocol.unpack(packed)
    assert remaining == b""
    assert packets[0][0] == 7
    assert packets[0][2] == {}


def test_unpack_two_packets_concat():
    """\u8fde\u7740\u53d1\u4e24\u4e2a\u5305 \u2014\u2014 unpack \u5e94\u4e00\u6b21\u8fd4\u56de\u4e24\u4e2a\u3002"""
    p1 = AGVProtocol.pack(1, 2001, {"a": 1})
    p2 = AGVProtocol.pack(2, 2002, {"b": 2})

    packets, remaining = AGVProtocol.unpack(p1 + p2)
    assert remaining == b""
    assert len(packets) == 2
    assert packets[0][0] == 1 and packets[0][1] == 2001
    assert packets[1][0] == 2 and packets[1][1] == 2002


def test_unpack_partial_packet():
    """\u5305\u88ab\u5207\u4e00\u534a \u2014\u2014 \u5e94\u8fd4\u56de\u7a7a\u5217\u8868 + \u539f\u59cb\u5269\u4f59 buffer\uff0c\u7b49\u540e\u7eed\u62fc\u63a5\u3002"""
    full = AGVProtocol.pack(99, 3001, {"x": "data"})
    partial = full[:-3]
    packets, remaining = AGVProtocol.unpack(partial)
    assert packets == []
    assert remaining == partial


def test_unpack_garbage_then_valid():
    """\u5269 buffer \u524d\u9762\u5e26\u4e1a\u52a1\u65e0\u5173\u7684\u5783\u573e\u5b57\u8282\uff0c\u5e94\u88ab\u4e22\u5f03\u5e76\u5bf9\u9f50\u5230 START_BYTE\u3002"""
    valid = AGVProtocol.pack(10, 4001, {"k": "v"})
    garbage = b"\x00\x11\x22\x33" + valid
    packets, remaining = AGVProtocol.unpack(garbage)
    assert remaining == b""
    assert len(packets) == 1
    assert packets[0][0] == 10


def test_unpack_oversized_body_len_resyncs():
    """\u4f2a\u9020\u4e00\u4e2a body_len \u8d85\u8fc7\u4e0a\u9650\u7684\u4f2a\u8d77\u59cb\u7b26\uff0c\u4e0d\u80fd\u51bb\u4f4f\u89e3\u6790\u5668\u3002"""
    import struct

    fake_header = struct.pack(
        "!BBHLH6s",
        START_BYTE,
        0x01,
        1,
        MAX_BODY_LEN + 1,
        9999,
        b"\x00" * 6,
    )
    valid = AGVProtocol.pack(20, 5001, {"ok": True})
    packets, _ = AGVProtocol.unpack(fake_header + valid)
    assert any(p[0] == 20 and p[1] == 5001 for p in packets)
