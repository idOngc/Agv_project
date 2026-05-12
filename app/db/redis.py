"""
Redis 客户端封装 —— 单例,异步,在 lifespan 启动期初始化。

约定:
  - 状态缓存键: `agv:{agv_id}:status`
  - 调度锁:    `lock:dispatch:{cp_uuid}`
"""

from __future__ import annotations

import logging

from redis.asyncio import Redis, from_url

from app.core.config import settings

log = logging.getLogger(__name__)

_redis: Redis | None = None


async def init_redis() -> Redis:
    global _redis
    if _redis is None:
        _redis = from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
        await _redis.ping()
        log.info("Redis connected: %s", settings.redis_url)
    return _redis


async def close_redis() -> None:
    global _redis
    if _redis is not None:
        await _redis.close()
        _redis = None
        log.info("Redis closed.")


def get_redis() -> Redis:
    if _redis is None:
        raise RuntimeError("Redis 未初始化,请先调用 init_redis() (lifespan 已自动调用)")
    return _redis
