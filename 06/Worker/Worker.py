from typing import Dict, List, Optional
import json
import requests

from bs4 import BeautifulSoup

from HTMLTextInforation.HTMLTextInformation import HTMLTextInformation


class Worker:
    tags_html = HTMLTextInformation.paragraphs_text_wrappers + HTMLTextInformation.headers
    special_symbols = HTMLTextInformation.special_symbols

    def __init__(self, url: str = ""):
        self.url = url
        if not url:
            self.soup_text = ""
            return
        try:
            html = requests.get(self.url).text
            soup = BeautifulSoup(html, "html5lib")
            self.soup_text: str = soup.text
        except requests.exceptions.ConnectionError as err:
            print(f"Error in Worker: {err}")

    def fetch_url(self, k: int = 10) -> Optional[str]:
        if not self.soup_text:
            return None
        result: Dict = {}
        list_test: List[str] = self.soup_text.split()
        for word in list_test:
            word = word.strip(self.special_symbols)
            if word:
                result[word] = result.get(word, 0) + 1
        if len(result.items()) < k:
            k = len(result.items())
        return json.dumps(
            dict(
                sorted(
                    result.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )[:k]
            ),
            ensure_ascii=False,
        )

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
