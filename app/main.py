"""
FastAPI 入口 —— 负责 lifespan(起启/关闭 Tortoise + Redis)、路由挂载、全局异常处理。

启动:
    uvicorn app.main:app --reload
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from tortoise import Tortoise

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.redis import close_redis, init_redis
from app.db.tortoise_conf import TORTOISE_ORM
from app.utils.exceptions import register_exception_handlers

setup_logging()
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    log.info("=== %s starting (env=%s) ===", settings.APP_NAME, settings.APP_ENV)
    await Tortoise.init(config=TORTOISE_ORM)
    log.info("Tortoise connected.")
    await init_redis()

    # TODO: 后续在这里启动 seer_manager.init_from_db() / status_poller 等

    try:
        yield
    finally:
        log.info("=== shutting down ===")
        # TODO: await seer_manager.close_all()
        await close_redis()
        await Tortoise.close_connections()


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan,
)

register_exception_handlers(app)
app.include_router(api_router)


@app.get("/health", tags=["meta"], summary="健康检查")
async def health() -> dict:
    return {"status": "ok", "app": settings.APP_NAME, "env": settings.APP_ENV}
