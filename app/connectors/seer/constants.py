"""
\u4ed9\u5de5 (SEER) Robokit \u7f51\u7edc\u534f\u8bae\u5e38\u91cf\u8868\u3002

\u6570\u636e\u6765\u6e90\uff1a\u4ed9\u5de5\u5b98\u65b9\u4ed3\u5e93 (\u4ec5\u4f9b\u53c2\u8003\uff0c\u540e\u7eed\u4ee5\u300aRobokit Netprotocol\u300b\u6587\u6863\u4e3a\u51c6):
    https://github.com/seer-robotics/Robokit_TCP_API_py
    https://github.com/seer-robotics/robokit_netprotocol_l   (\u4e2d\u6587\u8be6\u7ec6\u624b\u518c)

\u534f\u8bae\u62a5\u6587\u5934 (\u4e0e protocol.py \u4e2d HEADER_FMT \u4e00\u81f4):
    | 0x5A | Version(1B) | reqId(2B,BE) | jsonLen(4B,BE) | msgType(2B,BE) | reserved(6B) |
    \u540e\u63a5 jsonLen \u5b57\u8282 UTF-8 JSON \u4f53

\u7aef\u53e3 \u2194 API \u53f7\u6bb5\u8def\u7531\u89c4\u5219:
    1000-1999  \u2192 19204 (STATE)    \u72b6\u6001\u67e5\u8be2
    2000-2999  \u2192 19205 (CTRL)     \u63a7\u5236
    3000-3999  \u2192 19206 (TASK)     \u4efb\u52a1 / \u5bfc\u822a
    4000-5999  \u2192 19207 (CONFIG)   \u914d\u7f6e\u7ba1\u7406
    5100-5199  \u2192 19208 (KERNEL)   daemon \u6587\u4ef6\u4f20\u8f93 (ls/scp/rm)
    6000-6998  \u2192 19210 (OTHER)    \u6742\u9879 (DO/IO \u7b49)
"""

from __future__ import annotations

from enum import IntEnum


# ───────────────────────── \u7aef\u53e3 ─────────────────────────

class SeerPort(IntEnum):
    """\u4ed9\u5de5 Robokit \u5404\u529f\u80fd\u7aef\u53e3 (\u4e0e\u5b98\u65b9 rbkNetProtoEnums.py \u4e00\u81f4)\u3002"""
    ROBOD = 19200    # robod \u540e\u53f0\u670d\u52a1
    STATE = 19204    # \u72b6\u6001\u67e5\u8be2 (1000-1999)
    CTRL = 19205     # \u63a7\u5236 (2000-2999)
    TASK = 19206     # \u4efb\u52a1 / \u5bfc\u822a (3000-3999)
    CONFIG = 19207   # \u914d\u7f6e (4000-5999)
    KERNEL = 19208   # \u5185\u6838 / daemon (5100-5199)
    OTHER = 19210    # \u6742\u9879 (6000-6998)


# ────────────────────── msg_type \u5e38\u7528 API \u53f7 ──────────────────────
# \u8fd9\u91cc\u4ec5\u5217\u5b9e\u9645\u5728\u5b98\u65b9 Python demo \u91cc\u51fa\u73b0\u8fc7 / \u88ab\u660e\u786e\u70b9\u540d\u7684 API \u53f7\u3002
# \u540e\u7eed\u9700\u8981\u54ea\u4e2a\u518d\u52a0\u54ea\u4e2a\uff0c\u4e0d\u4e00\u6b21\u6027\u52a0\u4e00\u5806\u62a5\u6587\u91cc\u4ece\u672a\u7528\u8fc7\u7684\u3002

class StateMsg(IntEnum):
    """\u72b6\u6001\u67e5\u8be2 (\u7aef\u53e3 19204)\u3002"""
    INFO_REQ = 1000        # robot \u57fa\u672c\u4fe1\u606f (\u578b\u53f7 / SN \u7b49)
    RUN_REQ = 1002         # \u8fd0\u884c\u72b6\u6001 (\u662f\u5426\u52a8\u4f5c / \u662f\u5426\u963b\u6321 \u7b49)
    MODE_REQ = 1003        # \u5f53\u524d\u6a21\u5f0f (\u624b\u52a8 / \u81ea\u52a8)
    LOC_REQ = 1004         # \u4f4d\u59ff (x, y, angle, current_station ...)
    SPEED_REQ = 1005       # \u901f\u5ea6 (vx, vy, w)
    BATTERY_REQ = 1007     # \u7535\u91cf (battery_level \u7b49\uff0c\u53ef\u9644 {"simple": true})
    AREA_REQ = 1011        # \u533a\u57df\u4fe1\u606f
    IO_RES = 1013          # IO \u4e0a\u62a5
    TASK_REQ = 1020        # \u5f53\u524d\u4efb\u52a1\u72b6\u6001
    ALARM_RES = 1050       # \u544a\u8b66 \u4e0a\u62a5
    ALL1_REQ = 1100        # all-in-one \u72b6\u6001 \u5feb\u7167


class CtrlMsg(IntEnum):
    """\u63a7\u5236 (\u7aef\u53e3 19205)\u3002"""
    RELOC_REQ = 2002       # \u91cd\u5b9a\u4f4d {"x": ..., "y": ..., "angle": ...}
    MOTION_REQ = 2010      # \u8fd0\u52a8\u63a7\u5236 {"vx": .., "vy": .., "w": ..}


class TaskMsg(IntEnum):
    """\u4efb\u52a1 / \u5bfc\u822a (\u7aef\u53e3 19206)\u3002"""
    GOTARGET_REQ = 3051    # \u524d\u5f80\u76ee\u6807\u70b9 {"id": "AP1", "source_id": "...", "task_id": "..."}


class KernelMsg(IntEnum):
    """daemon (\u7aef\u53e3 19208)\u3002\u8c03\u8bd5 / \u8fd0\u7ef4\u7528\uff0c\u4e1a\u52a1\u7aef\u4e00\u822c\u4e0d\u52a8\u3002"""
    DAEMON_LS_REQ = 5100
    DAEMON_SCP_REQ = 5101
    DAEMON_RM_REQ = 5102


class OtherMsg(IntEnum):
    """\u6742\u9879 (\u7aef\u53e3 19210)\u3002"""
    SETDO_REQ = 6001       # \u8bbe\u7f6e\u6570\u5b57\u8f93\u51fa


# ────────────────────── msg_type \u2192 \u7aef\u53e3 \u8def\u7531 ──────────────────────

def port_for(msg_type: int) -> SeerPort:
    """
    \u6839\u636e msg_type \u8fd4\u56de\u5e94\u8be5\u8d70\u54ea\u4e2a\u7aef\u53e3\u3002

    \u8fd9\u4e2a\u51fd\u6570\u662f\u8fde\u63a5\u5c42\u8def\u7531\u7684\u552f\u4e00\u6743\u5a01\u6e90\uff0c\u4e0a\u5c42\u4e0d\u7ba1\u8fde\u54ea\u4e2a socket\u3002

    >>> port_for(1004)
    <SeerPort.STATE: 19204>
    >>> port_for(3051)
    <SeerPort.TASK: 19206>
    """
    if 1000 <= msg_type <= 1999:
        return SeerPort.STATE
    if 2000 <= msg_type <= 2999:
        return SeerPort.CTRL
    if 3000 <= msg_type <= 3999:
        return SeerPort.TASK
    if 4000 <= msg_type <= 5099:
        return SeerPort.CONFIG
    if 5100 <= msg_type <= 5199:
        return SeerPort.KERNEL
    if 5200 <= msg_type <= 5999:
        return SeerPort.CONFIG
    if 6000 <= msg_type <= 6998:
        return SeerPort.OTHER
    raise ValueError(f"Unknown SEER msg_type: {msg_type}")


# \u5176\u5b83\u9ed8\u8ba4\u53c2\u6570

DEFAULT_REQ_TIMEOUT: float = 5.0       # \u5355\u6b21\u8bf7\u6c42\u8d85\u65f6 (\u79d2)
RECV_BUFFER_SIZE: int = 4096            # \u5355\u6b21 recv \u8bfb\u53d6\u4e0a\u9650
HEARTBEAT_INTERVAL: float = 3.0         # \u5fc3\u8df3\u8f6e\u8be2\u95f4\u9694 (\u79d2)
