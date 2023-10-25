#!/usr/bin/env python3
"""
    Fifo cache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO cache class
        inherits from BaseCashing
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assigns to the dictionary self.cache_data
            the item value for the key key
        """
        if key and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                f_key = next(iter(self.cache_data))
                del self.cache_data[f_key]
                print("DISCARD: {}".format(f_key))

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
