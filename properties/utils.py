from django.core.cache import cache
from .models import Property
import redis
from django.conf import settings
import logging

def get_all_properties():
    query_set = cache.get('all_properties')

    if not query_set:
        query_set = Property.objects.all()
        cache.set('all_properties', query_set, 3600)
    return query_set

logger = logging.getLogger(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

def get_redis_cache_metrics():
    try:
        info = r.info('stats')
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "total_requests": total_requests,
            "hit_ratio": round(hit_ratio, 4)
        }

        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics
    
    except redis.exceptions.RedisError as e:
        logger.error(f"Redis error while retrieving metrics: {str(e)}")
        return {
            "error": "Failed to retrieve Redis metrics",
            "details": str(e)
        }