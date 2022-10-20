from typing import Dict
from urllib.request import urlopen


class Worker:
    def __init__(self, url: str):
        self.url = url

    def fetch_url(self) -> Dict:
        result: Dict = {}
        with urlopen(self.url) as resp:
            for line in resp:
                line_decode = line.decode('utf-8').strip().split()
                for word in line_decode:
                    if word:
                        pass

            # for line in resp.read().decode('utf-8'):
            #     print(line)
            # print(resp.read().decode('utf-8'))
        return result


#
#
#
# URL = "https://ru.wikipedia.org/wiki/Python"
# N = 100
#
#
# def fetch_url(url):
#     resp = urlopen(url)
#     return resp
#
#
# def fetch_batch_urls(url, times):
#     for _ in range(times):
#         resp = fetch_url(url)
#
#
# N_THREADS = 10
#
#
# threads = [
#     threading.Thread(
#         target=fetch_batch_urls,
#         args=(URL, N // N_THREADS,),
#     )
#     for _ in range(N_THREADS)
# ]
#
# for th in threads:
#     th.start()
#
# for th in threads:
#     th.join()
