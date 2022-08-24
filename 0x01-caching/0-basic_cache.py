#!usr/bin/env python3
"""
Defines a class BasicCache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    def put(self, key, item):
        """
        Assigns the item value for the key in the
        dictionary self.cache_data
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data
        linked to key
        """
        if key is None:
            return None
        gotten_key = self.cache_data.get(key)
        if gotten_key is None:
            return None
        return gotten_key
