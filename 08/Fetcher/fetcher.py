from typing import List
import asyncio
import aiohttp


async def fetch(result_data: List,
                session: aiohttp.ClientSession,
                async_queue: asyncio.Queue,
                ):
    while True:
        url = await async_queue.get()
        try:
            async with session.get(url) as resp:
                data: bytes = await resp.read()
                assert resp.status == 200
                result_data.append(data)
        finally:
            async_queue.task_done()


async def batch_fetch(result_data: List, urls: List, workers: int = 1):
    async_queue = asyncio.Queue()
    for url in urls:
        await async_queue.put(url)

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch(result_data, session, async_queue))
            for _ in range(workers)
        ]
        await async_queue.join()

        for worker in workers:
            worker.cancel()
