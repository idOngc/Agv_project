"""\u4efb\u52a1\u4e0b\u53d1 / \u67e5\u8be2 schema\u3002\u4e0e models/task.py \u4fdd\u6301\u4e00\u81f4\u3002"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.models.task import TaskStatus, TaskType


class TaskCreateIn(BaseModel):
    agv_uuid: str = Field(..., description="\u76ee\u6807 AGV \u7684 uuid")
    type: TaskType = TaskType.NAVIGATE
    target_point: str = Field(..., description="\u76ee\u6807\u70b9\u4f4d\u540d, e.g. AP6")
    payload: dict[str, Any] = Field(default_factory=dict)


class TaskOut(BaseModel):
    id: int
    uuid: str
    type: TaskType
    target_point: str
    status: TaskStatus
    error_msg: str | None = None
    created_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None

    class Config:
        from_attributes = True
