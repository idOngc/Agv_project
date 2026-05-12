"""任务下发 / 查询 schema。与 models/task.py 保持一致。"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.models.task import TaskStatus, TaskType


class TaskCreateIn(BaseModel):
    agv_uuid: str = Field(..., description="目标 AGV 的 uuid")
    type: TaskType = TaskType.NAVIGATE
    target_point: str = Field(..., description="目标点位名, e.g. AP6")
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
