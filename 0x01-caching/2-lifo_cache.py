#!/usr/bin/python3
"""
    LIFO caching class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFO cache class
        inherits form BaseCaching
    """
    def __init__(self):
        super().__init__()
        self._last_item = None

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key
        """
        if item and key is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    print("Discard: {}".format(self._last_item))
                    del self.cache_data[self._last_item]
            self.cache_data[key] = item
            self.last_item = key

    def get(self, key):
        """
            Returns the value in self.cache_data linked to key
        """
        try:
            value = self.cache_data[key]
            self._last_item = key
            return value
        except KeyError:
            return None
