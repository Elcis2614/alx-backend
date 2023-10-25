#!/usr/bin/env python3
"""
    Basic cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assigns the dictionary cache_data
            defined in parent class
        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
