"""
FastAPI \u5165\u53e3 \u2014\u2014 \u8d1f\u8d23 lifespan(\u8d77\u542f/\u5173\u95ed Tortoise + Redis)\u3001\u8def\u7531\u6302\u8f7d\u3001\u5168\u5c40\u5f02\u5e38\u5904\u7406\u3002

\u542f\u52a8:
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

    # TODO: \u540e\u7eed\u5728\u8fd9\u91cc\u542f\u52a8 seer_manager.init_from_db() / status_poller \u7b49

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


@app.get("/health", tags=["meta"], summary="\u5065\u5eb7\u68c0\u67e5")
async def health() -> dict:
    return {"status": "ok", "app": settings.APP_NAME, "env": settings.APP_ENV}
