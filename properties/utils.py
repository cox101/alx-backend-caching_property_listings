from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    try:
        conn = get_redis_connection("default")
        info = conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 2)
        }

        logger.info(f"Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Failed to fetch Redis metrics: {str(e)}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0
        }
