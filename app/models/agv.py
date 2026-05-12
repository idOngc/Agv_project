"""
AGV \u8bbe\u5907\u8868 \u2014\u2014 \u5bf9\u9f50\u300aAGV \u6570\u636e\u7ed3\u6784\u300b\u6587\u6863\u91cc\u7684 AGV \u5b9a\u4e49\uff0c\u6700\u5c0f\u7248\u53ea\u4fdd\u7559\u8868\u8fbe
\u8fde\u63a5\u6240\u9700\u7684\u5b57\u6bb5\u3002\u8df3\u8f66 / \u5145\u7535 / \u62fc\u5355 \u9608\u503c\u7b49\u540e\u7eed\u518d\u6dfb\u3002
"""

from enum import IntEnum

from tortoise import fields
from tortoise.models import Model


class AGVMode(IntEnum):
    FORKLIFT = 1    # \u53c9\u8f66
    JACK = 2        # \u9876\u5347\u8f66
    TRACTOR = 3     # \u62d6\u8f66
    FLIPPER = 4     # \u7ffb\u8f6c\u8f66


class AGVProtocolType(IntEnum):
    TCP_IP = 1
    MODBUS_TCP = 2


class AGV(Model):
    id = fields.IntField(pk=True)
    uuid = fields.CharField(max_length=64, unique=True, description="\u5168\u5c40\u552f\u4e00 ID (\u4f5c\u4e3a deviceId)")
    name = fields.CharField(max_length=64, description="\u663e\u793a\u540d, e.g. LPT-AGV-J01")

    mode = fields.IntEnumField(AGVMode, default=AGVMode.JACK)
    protocol = fields.IntEnumField(AGVProtocolType, default=AGVProtocolType.TCP_IP)
    vendor_type = fields.CharField(max_length=32, default="seer_amb", description="\u53a8\u5546\u578b\u53f7")

    ip = fields.CharField(max_length=64)
    # \u4ed9\u5de5 AGV \u7aef\u53e3\u8868 (\u53ef\u4ee5\u91cd\u5199): \u72b6\u6001/\u5bfc\u822a/\u63a7\u5236/\u914d\u7f6e/\u63a8\u9001
    port_status = fields.IntField(default=19204)
    port_nav = fields.IntField(default=19205)
    port_control = fields.IntField(default=19206)
    port_config = fields.IntField(default=19207)
    port_push = fields.IntField(default=19301)

    is_active = fields.BooleanField(default=True, description="\u662f\u5426\u542f\u7528")

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "agv"

    def __str__(self) -> str:
        return f"<AGV {self.name} {self.ip}>"
