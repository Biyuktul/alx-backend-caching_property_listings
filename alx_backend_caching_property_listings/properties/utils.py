from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all Property objects using caching for efficiency.

    - Checks if a cached list of Property IDs exists.
    - If cached IDs exist, returns a QuerySet of Properties matching those IDs.
    - If not, fetches all Property IDs from the database, caches them for one hour, and returns the corresponding QuerySet.
    - Always returns a QuerySet.
    """
    property_ids = cache.get('all_properties')

    if property_ids is None:
        property_ids = list(Property.objects.values_list('id', flat=True))
        cache.set('all_properties', property_ids, 3600)
    return Property.objects.filter(id__in=property_ids) # returning a queryset


# def get_all_properties():
#     properties = cache.get('all_properties')
#     if properties is None:
#         properties = list(Property.objects.all())
#         cache.set('all_properties', properties, 3600)
#     return properties

import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss statistics and calculate the hit ratio.

    Returns:
        dict: {
            "hits": int,
            "misses": int,
            "hit_ratio": float (0.0-1.0 or None if no accesses)
        }
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) if total else None

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }

    logger.info(
        "Redis Cache Metrics - Hits: %d, Misses: %d, Hit Ratio: %s",
        hits, misses, f"{hit_ratio:.2%}" if hit_ratio is not None else "N/A"
    )
    return metrics