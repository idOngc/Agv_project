"""
统一日志配置 —— 在 main.py 启动时调用一次 setup_logging()。
"""

import logging
import sys

from app.core.config import settings


def setup_logging() -> None:
    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    fmt = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(fmt))

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)

    for noisy in ("asyncmy", "tortoise", "uvicorn.access"):
        logging.getLogger(noisy).setLevel(max(level, logging.INFO))
