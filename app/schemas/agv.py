"""AGV 资源的请求 / 响应 schema。字段命名与 models.agv.AGV 保持一致。"""

from pydantic import BaseModel


class AGVCreateIn(BaseModel):
    uuid: str
    name: str
    ip: str
    port_state: int = 19204
    port_ctrl: int = 19205
    port_task: int = 19206
    port_config: int = 19207
    port_other: int = 19210


class AGVOut(BaseModel):
    id: int
    uuid: str
    name: str
    ip: str
    is_active: bool

    class Config:
        from_attributes = True
