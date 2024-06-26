#!/usr/bin/env python3
"""1-fifo_cache.py"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """a fifo cache system"""
    def __init__(self):
        """instantiate an object"""
        super().__init__()
        self.fifo = []  # stores the keys to mimic the FIFO algorithm

    def put(self, key, item):
        """Add an item to the cache using FIFO algo"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = self.fifo.pop(0)
            self.cache_data.pop(k)
            print(f"DISCARD: {k}")
        self.cache_data.update({key: item})
        self.fifo.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
