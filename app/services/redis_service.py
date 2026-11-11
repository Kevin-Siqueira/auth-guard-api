import redis
from app.core.config import settings

# Conexão com o servidor Redis
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    decode_responses=True
)

class RedisService:
    @staticmethod
    def add_token_to_blacklist(token: str, expire_seconds: int) -> None:
        """Adiciona o token à blacklist no Redis com tempo de expiração (TTL)."""
        redis_client.setex(name=f"blacklist:{token}", time=expire_seconds, value="true")

    @staticmethod
    def is_token_blacklisted(token: str) -> bool:
        """Verifica se o token consta na blacklist do Redis."""
        return redis_client.exists(f"blacklist:{token}") == 1