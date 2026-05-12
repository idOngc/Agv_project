"""
\u4e1a\u52a1\u5f02\u5e38\u57fa\u7c7b + FastAPI \u5168\u5c40\u5f02\u5e38\u5904\u7406\u5668\u3002

\u5728 main.py \u91cc\u8c03 register_exception_handlers(app)\u3002
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    """\u4e1a\u52a1\u5c42\u53ef\u9884\u671f\u5f02\u5e38\u7684\u57fa\u7c7b\u3002"""

    code: int = 1000
    msg: str = "app error"
    http_status: int = 400

    def __init__(self, msg: str | None = None, *, code: int | None = None, http_status: int | None = None):
        super().__init__(msg or self.msg)
        self.msg = msg or self.msg
        if code is not None:
            self.code = code
        if http_status is not None:
            self.http_status = http_status


class AGVNotFound(AppError):
    code = 2001
    msg = "AGV not found"
    http_status = 404


class AGVOffline(AppError):
    code = 2002
    msg = "AGV offline / unreachable"
    http_status = 503


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def _handle_app_error(_: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.http_status,
            content={"code": exc.code, "msg": exc.msg, "data": None},
        )
