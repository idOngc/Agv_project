"""
仙工 (SEER) AGV 端口与 msg_type 常量表。

> ⚠️ 下面的 msg_type 是「骨架示例」，实际数值以仙工官方文档为准。
> 请在下一轮以仙工 wiki的「端口 / 请求号 / 功能」对照表补齐后取代这些 TODO。

仙工端口职责 (通用约定):
    19204   状态查询   robot status (电量 / 坐标 / 错误码 等)
    19205   导航       navigation
    19206   控制       任务 / 动作 / 手动控制
    19207   配置       configure (地图 / 参数)
    19208   设备推送
    19210   其他 API
    19301   实时推送 push (server 主动发)
"""

from enum import IntEnum


class SeerPort(IntEnum):
    STATUS = 19204
    NAV = 19205
    CONTROL = 19206
    CONFIG = 19207
    PUSH_SETTING = 19208
    OTHER = 19210
    PUSH = 19301


class StatusMsgType(IntEnum):
    """端口 19204 上的查询类报文。数值待仙工文档补齐。"""
    QUERY_ROBOT_STATUS_ALL = 0       # TODO: 实际值
    QUERY_BATTERY = 0                # TODO
    QUERY_POSITION = 0               # TODO


class NavMsgType(IntEnum):
    """端口 19205 上的导航报文。"""
    NAVIGATE_TO_POINT = 0            # TODO: e.g. 3051
    PAUSE = 0                        # TODO
    RESUME = 0                       # TODO
    CANCEL = 0                       # TODO


class ControlMsgType(IntEnum):
    """端口 19206 上的动作报文。"""
    JACK_LOAD = 0                    # TODO
    JACK_UNLOAD = 0                  # TODO
    JACK_HEIGHT = 0                  # TODO


# 请求超时 (秒)，不同报文可在高层 api 里重写
DEFAULT_REQ_TIMEOUT: float = 5.0
