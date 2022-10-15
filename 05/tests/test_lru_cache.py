from LRUCache.LRUCache import LRUCache


def test_default():
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert not cache.get("k3")
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert not cache.get("k2")
    assert cache.get("k1") == "val1"


def test_limit_one_item():
    cache = LRUCache(1)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k2")
    assert not cache.get("k1")


def test_many_request():
    cache = LRUCache(2)

    cache.set("k1", "val1")
    for _ in range(999):
        cache.get("k1")
    assert cache.get("k1")
    assert cache.lru["k1"] == 1000
    assert cache.cache["k1"] == "val1"
