#!/usr/bin/python3
"""
    MRU caching class
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        MRU cache class
        inherits form BaseCaching
    """
    def __init__(self):
        super().__init__()
        self._most_key = None

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key
        """
        if item and key is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    print("DISCARD: {}".format(self._most_key))
                    del self.cache_data[self._most_key]
            self.cache_data[key] = item
            self._most_key = key

    def get(self, key):
        """
            Returns the value in self.cache_data linked to key
        """
        try:
            value = self.cache_data[key]
            self._most_key = key
            return value
        except KeyError:
            return None
