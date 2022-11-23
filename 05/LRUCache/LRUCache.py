from typing import Dict, Hashable, Optional, Any
from collections import OrderedDict


class LRUCache:
    def __init__(self, limit: int) -> None:
        self.limit: int = limit
        self.time_: int = 0
        self.cache: Dict[Hashable, Any] = {}
        self.lru: Dict[Hashable, int] = {}

    def get(self, key: Hashable) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.lru[key] = self.time_
        self.time_ += 1
        return self.cache[key]

    def set(self, key: Hashable, value: Any) -> None:
        if key in self.cache and self.cache[key] == value:
            self.lru[key] = self.time_
            self.time_ += 1
            return
        if len(self.cache) >= self.limit:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            old_key_number = self.lru[old_key]
            self.cache.pop(old_key)
            self.lru.pop(old_key)
            for key_ in self.lru:
                self.lru[key_] -= old_key_number
            self.time_ = 0
        self.cache[key] = value
        self.lru[key] = self.time_
        self.time_ += 1


class LRUCacheOrderDict:
    def __init__(self, capacity: int):
        self.cache: OrderedDict = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: Hashable) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: Hashable, value: Any) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
