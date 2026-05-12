"""AGV \u8d44\u6e90\u7684\u8bf7\u6c42 / \u54cd\u5e94 schema\u3002\u540e\u7eed\u6309\u9700\u6269\u5145\u3002"""

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
