#!/usr/bin/env python3
"""3-lru_cache.py"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """a lru cache system"""
    def __init__(self):
        """initialize an LRU cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using LRU algo"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # move the existing item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # pop the first item (least recently used item)
            o_k, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {o_k}")

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        # move the accessed item to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
