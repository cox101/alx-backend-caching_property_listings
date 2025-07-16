from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    ratio = hits / (hits + misses) if (hits + misses) > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(ratio, 2)
    }

    logger.info(f"Cache metrics: {metrics}")
    return metrics
