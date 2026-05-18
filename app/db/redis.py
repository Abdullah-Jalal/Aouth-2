import logging
import time
from collections.abc import AsyncGenerator
from typing import Any

from redis.asyncio import Redis
from redis.exceptions import ConnectionError as RedisConnectionError

from app.core.config import settings

logger = logging.getLogger(__name__)


class RedisMock:
    """A tiny async in-memory Redis-like fallback used when Redis isn't available.

    It implements the subset used by this project: `ping`, `set`, `get`, and `aclose`.
    Expiry (`ex`) is supported in seconds for blacklist entries.
    """

    def __init__(self) -> None:
        self._store: dict[str, tuple[Any, float | None]] = {}

    async def ping(self) -> bool:  # pragma: no cover - trivial
        return True

    async def set(self, key: str, value: Any, ex: int | None = None) -> None:
        expire_at = time.time() + ex if ex else None
        self._store[key] = (value, expire_at)

    async def get(self, key: str) -> Any | None:
        item = self._store.get(key)
        if not item:
            return None
        value, expire_at = item
        if expire_at is not None and time.time() > expire_at:
            # expired
            self._store.pop(key, None)
            return None
        return value

    async def aclose(self) -> None:  # pragma: no cover - trivial
        self._store.clear()


redis_client: Redis | RedisMock | None = None


async def connect_redis() -> None:
    """Try to connect to a real Redis server, otherwise fall back to RedisMock.

    This prevents application startup from failing when Redis is not present
    (useful for local development without Redis)."""
    global redis_client

    try:
        redis_client = Redis.from_url(
            settings.redis_url,
            decode_responses=True,
        )
        await redis_client.ping()
        logger.info("Connected to Redis at %s", settings.redis_url)
    except RedisConnectionError as exc:
        logger.warning(
            "Could not connect to Redis (%s); using in-memory fallback.",
            exc,
        )
        redis_client = RedisMock()


async def close_redis() -> None:
    if redis_client:
        await redis_client.aclose()


async def get_redis() -> AsyncGenerator[Redis | RedisMock]:
    if not redis_client:
        raise RuntimeError("Redis client is not initialized")

    yield redis_client
