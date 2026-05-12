"""
\u901a\u7528\u54cd\u5e94\u4f53 / \u5206\u9875\u53c2\u6570\u3002
"""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class Resp(BaseModel, Generic[T]):
    code: int = 0
    msg: str = "ok"
    data: T | None = None


class PageQuery(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=200)


class PageResult(BaseModel, Generic[T]):
    total: int
    page: int
    page_size: int
    items: list[T]
