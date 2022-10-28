import threading
import os.path
from typing import List, Dict

import click

from Client.Client import Client


def fetch_url(url):
    client = Client("localhost", 8888)
    client.send(url[:-1])
    return client.read()


def fetch_batch_urls(url_list):
    for url in url_list:
        res = fetch_url(url)
        print(res)


@click.command()
@click.option('--file', default="", help="File containing url")
@click.option('--M', default=1, help="Number of threads.")
def send_requests(file: str, m: int, n: int = 10):
    if not os.path.isfile(file):
        print("File not exist")
        return None
    urls: List[str] = []
    with open(file, "r") as _file:
        for line in _file:
            urls.append(line)
    # print(urls)
    url_dict: Dict[int, List[str]] = {}
    for ind in range(m):
        for elem in range(0, n, ind + 1):
            url_dict[ind] = urls[ind * n // m:n // m * (ind + 1)]
    if m % 2 == 1:
        url_dict[m - 1].append(urls[-1])
    threads = [
        threading.Thread(
            target=fetch_batch_urls,
            args=(url_dict[ind],),
        )
        for ind in range(m)
    ]
    for th in threads:
        th.start()
    for th in threads:
        th.join()


if __name__ == "__main__":
    send_requests()
