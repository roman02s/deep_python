import time
import asyncio

import click

from Fetcher.fetcher import batch_fetch


@click.command()
@click.argument('count_workers', default=1)
@click.argument('urls_path', default="tests/static/urls.txt")
def send_requests(count_workers: int, urls_path: str) -> None:
    urls = []
    with open(urls_path, "r", encoding="utf-8") as file:
        for line in file:
            urls.append(line[:-1])
    result_data = []
    t_start = time.time()
    asyncio.run(batch_fetch(result_data, urls, count_workers))
    t_end = time.time()
    print("time", t_end - t_start)


if __name__ == "__main__":
    send_requests()
