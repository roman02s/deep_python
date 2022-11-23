import time
import asyncio

import click

from Fetcher.fetcher import batch_fetch
from Fetcher.fetcher import fetch
from aiohttp_test import AioHttpBase


def test_fetch():
    aiohttp = AioHttpBase
    result = []
    queue = asyncio.Queue()
    queue.put("test url")
    aiohttp.ClientSession().get(queue.get()).read()
    fetch(result, aiohttp.ClientSession(), queue)
    assert result == [b"test data"]
