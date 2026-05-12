"""
\u4efb\u52a1\u8868 \u2014\u2014 \u6700\u5c0f\u7248\u53ea\u8bb0\u5f55\u300c\u4e0b\u53d1\u8fc7\u4ec0\u4e48 / \u72b6\u6001 / \u54ea\u53f0\u8f66\u300d\u3002

\u540e\u7eed\u4f1a\u62c6\u51fa Task / TaskStep \u4e24\u8868\uff0c\u5bf9\u9f50\u6587\u6863\u4e2d\u7684 taskTemplate.steps[]\u3002
"""

from enum import IntEnum

from tortoise import fields
from tortoise.models import Model


class TaskStatus(IntEnum):
    INIT = 0
    RUNNING = 1
    COMPLETED = 2
    FAILED = 3
    CANCELED = 4


class TaskType(IntEnum):
    """\u6700\u5c0f\u7248\u5148\u7528\u4e09\u79cd\uff0c\u540e\u7eed\u8865\u9f50\u6587\u6863\u91cc\u7684\u62d6\u96b6/\u63a7\u5236\u7b49\u3002"""
    NAVIGATE = 1        # \u7eaf\u5bfc\u822a
    JACK_LOAD = 2       # \u9876\u5347\u53d6\u8d27
    JACK_UNLOAD = 3     # \u9876\u5347\u653e\u8d27


class Task(Model):
    id = fields.IntField(pk=True)
    uuid = fields.CharField(max_length=64, unique=True, description="\u4efb\u52a1\u5168\u5c40 ID")

    agv = fields.ForeignKeyField("models.AGV", related_name="tasks", on_delete=fields.RESTRICT)

    type = fields.IntEnumField(TaskType)
    target_point = fields.CharField(max_length=64, description="\u76ee\u6807\u70b9\u540d (\u5730\u56fe\u70b9\u4f4d)")
    payload = fields.JSONField(default=dict, description="\u4efb\u52a1\u989d\u5916\u53c2\u6570")

    status = fields.IntEnumField(TaskStatus, default=TaskStatus.INIT)
    error_msg = fields.CharField(max_length=512, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    started_at = fields.DatetimeField(null=True)
    finished_at = fields.DatetimeField(null=True)

    class Meta:
        table = "task"
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"<Task#{self.id} {self.type.name} -> {self.target_point} [{self.status.name}]>"
