#!/usr/bin/env python3
"""
    LRUCache class
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        LRU Cache algorithm
    """
    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key.
        """
        if key and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                f_key = next(iter(self.cache_data))
                del self.cache_data[f_key]
                print("DISCARD: {}".format(f_key))

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key
            and refresh the cache
        """
        try:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        except KeyError:
            return None
