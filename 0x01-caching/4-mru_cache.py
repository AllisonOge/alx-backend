#!/usr/bin/env python3
"""4-mru_cache.py"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """a mru cache"""
    def __init__(self):
        """initialize an MRU cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using MRU algo"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # pop the last item (most recently used item)
            o_k, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {o_k}")

        self.cache_data.update({key: item})
        # move the existing item to the end to mark it as recently used
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        # move the accessed item to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
