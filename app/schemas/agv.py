"""AGV 资源的请求 / 响应 schema。后续按需扩充。"""

from pydantic import BaseModel, Field


class AGVCreateIn(BaseModel):
    uuid: str
    name: str
    ip: str
    port_status: int = 19204
    port_nav: int = 19205
    port_control: int = 19206


class AGVOut(BaseModel):
    id: int
    uuid: str
    name: str
    ip: str
    is_active: bool

    class Config:
        from_attributes = True
