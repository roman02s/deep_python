from typing import Dict, List, Optional
import re
import json

import requests
from bs4 import BeautifulSoup

from HTMLTextInforation.HTMLTextInformation import HTMLTextInformation


class Worker:
    tags_html = HTMLTextInformation.paragraphs_text_wrappers + HTMLTextInformation.headers
    special_symbols = HTMLTextInformation.special_symbols

    def __init__(self, url: str):
        self.url = url
        try:
            html = requests.get(self.url).text
            self.soup = BeautifulSoup(html, "html5lib")
        except requests.exceptions.ConnectionError as err:
            print(f"Error in Worker: {err}")

    def fetch_url(self, k: int = 10) -> Optional[str]:
        if not self.soup:
            return None
        result: Dict = {}
        list_test = self.soup.text.split()
        for word in list_test:
            word = word.strip(self.special_symbols)
            if word:
                result[word] = result.get(word, 0) + 1
        if len(result.items()) < k:
            k = len(result.items())
        return json.dumps(
            dict(sorted(result.items(),
                        key=lambda item: item[1])[-k:]),
            ensure_ascii=False,
        )

    def get_urls(self) -> Optional[List]:
        if not self.soup:
            return None
        all_urls = [a["href"] for a in self.soup("a") if a.has_attr("href")]
        regex = r"https?://"
        good_urls = [url for url in all_urls if re.match(regex, url)]
        return good_urls
