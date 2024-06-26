#!/usr/bin/env python3
"""2-lifo_cache.py"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """a lifo cache system"""
    def __init__(self):
        """instantiate an object"""
        super().__init__()
        self.lifo = []  # stores the keys to mimic the LIFO algorithm

    def put(self, key, item):
        """Add an item to the cache using LIFO algo"""
        if key is None or item is None:
            return
        if key not in self.cache_data \
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = self.lifo.pop()
            self.cache_data.pop(k)
            print(f"DISCARD: {k}")
        self.cache_data.update({key: item})
        self.lifo.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
