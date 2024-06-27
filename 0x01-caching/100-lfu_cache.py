#!/usr/bin/env python3
"""100-lfu_cache.py"""
from collections import defaultdict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """a lfu cache"""
    def __init__(self):
        super().__init__(self)
        self.frequency = defaultdict(int)  # tracks the frequency of each item

    def put(self, key, item):
        """Add an item to the cache using LFU algorithm"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data:
                    # fimd the least frequency used item
                    lfui = min(self.frequency.values())
                    lfuk = [k for k, v in self.frequency.items() if v == lfui][0]
                    self.cache_data.pop(lfuk)
                    self.frequency.pop(lfuk)
                    print(f"DISCARD: {lfuk}")
        self.cache_data.update({key: item})
        self.frequency[key] += 1

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1  # inc the frequency of access
        return self.cache_data.get(key)
