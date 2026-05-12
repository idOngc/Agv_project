"""
\u4ed9\u5de5 (SEER) AGV \u7aef\u53e3\u4e0e msg_type \u5e38\u91cf\u8868\u3002

> \u26a0\ufe0f \u4e0b\u9762\u7684 msg_type \u662f\u300c\u9aa8\u67b6\u793a\u4f8b\u300d\uff0c\u5b9e\u9645\u6570\u503c\u4ee5\u4ed9\u5de5\u5b98\u65b9\u6587\u6863\u4e3a\u51c6\u3002
> \u8bf7\u5728\u4e0b\u4e00\u8f6e\u4ee5\u4ed9\u5de5 wiki\u7684\u300c\u7aef\u53e3 / \u8bf7\u6c42\u53f7 / \u529f\u80fd\u300d\u5bf9\u7167\u8868\u8865\u9f50\u540e\u53d6\u4ee3\u8fd9\u4e9b TODO\u3002

\u4ed9\u5de5\u7aef\u53e3\u804c\u8d23 (\u901a\u7528\u7ea6\u5b9a):
    19204   \u72b6\u6001\u67e5\u8be2   robot status (\u7535\u91cf / \u5750\u6807 / \u9519\u8bef\u7801 \u7b49)
    19205   \u5bfc\u822a       navigation
    19206   \u63a7\u5236       \u4efb\u52a1 / \u52a8\u4f5c / \u624b\u52a8\u63a7\u5236
    19207   \u914d\u7f6e       configure (\u5730\u56fe / \u53c2\u6570)
    19208   \u8bbe\u5907\u63a8\u9001
    19210   \u5176\u4ed6 API
    19301   \u5b9e\u65f6\u63a8\u9001 push (server \u4e3b\u52a8\u53d1)
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
    """\u7aef\u53e3 19204 \u4e0a\u7684\u67e5\u8be2\u7c7b\u62a5\u6587\u3002\u6570\u503c\u5f85\u4ed9\u5de5\u6587\u6863\u8865\u9f50\u3002"""
    QUERY_ROBOT_STATUS_ALL = 0       # TODO: \u5b9e\u9645\u503c
    QUERY_BATTERY = 0                # TODO
    QUERY_POSITION = 0               # TODO


class NavMsgType(IntEnum):
    """\u7aef\u53e3 19205 \u4e0a\u7684\u5bfc\u822a\u62a5\u6587\u3002"""
    NAVIGATE_TO_POINT = 0            # TODO: e.g. 3051
    PAUSE = 0                        # TODO
    RESUME = 0                       # TODO
    CANCEL = 0                       # TODO


class ControlMsgType(IntEnum):
    """\u7aef\u53e3 19206 \u4e0a\u7684\u52a8\u4f5c\u62a5\u6587\u3002"""
    JACK_LOAD = 0                    # TODO
    JACK_UNLOAD = 0                  # TODO
    JACK_HEIGHT = 0                  # TODO


# \u8bf7\u6c42\u8d85\u65f6 (\u79d2)\uff0c\u4e0d\u540c\u62a5\u6587\u53ef\u5728\u9ad8\u5c42 api \u91cc\u91cd\u5199
DEFAULT_REQ_TIMEOUT: float = 5.0
