#!/usr/bin/env python3
"""
    LFU cach class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        LFU class inherits BaseCaching
    """
    def __init__(self):
        super().__init__()
        self._keys = {}

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key
        """
        if key and item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            freq = self._keys[key]
            del self._keys[key]
            self._keys[key] = freq + 1
            return
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                leastF = 999999
                leastKey = 0
                for lkey, value in self._keys.items():
                    if value <= leastF:
                        leastKey = lkey
                        leastF = value
                del self._keys[leastKey]
                del self.cache_data[leastKey]
                print("DISCARD: {}".format(leastKey))
            self.cache_data[key] = item
            self._keys[key] = 1

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        try:
            freq = self._keys[key]
            del self._keys[key]
            self._keys[key] = freq + 1
            return self.cache_data[key]
        except KeyError:
            return None
