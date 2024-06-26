#!/usr/bin/env python3
"""0-basic_cache.py"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """a basic cache system"""
    def put(self, key, item):
        """Add item to the cache without limit"""
        if key is None and item is None:
            return
        self.cache_data.update({f"{key}": item})

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return
        return self.cache_data.get(key)
