import string
from typing import Dict, List, Optional
import json
import requests

from bs4 import BeautifulSoup

from HTMLTextInforation.HTMLTextInformation import HTMLTextInformation


class Worker:
    tags_html = HTMLTextInformation.paragraphs_text_wrappers + HTMLTextInformation.headers
    special_symbols = HTMLTextInformation.special_symbols + string.digits

    def __init__(self, url: str = ""):
        self.url = url
        if not url:
            self.soup_text = ""
            return
        try:
            html = requests.get(self.url).text
            soup = BeautifulSoup(html, "html5lib")
            # self.soup_text: str = str(soup.find_all(self.tags_html))
            self.soup_text: str = soup.text
        except requests.exceptions.ConnectionError as err:
            print(f"Error in Worker: {err}")

    def fetch_url(self, k: int = 10) -> Optional[str]:
        if hasattr(self, "soup_text") and not self.soup_text:
            return None
        result: Dict = self._parse_soup_text()
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

    def _parse_soup_text(self) -> Dict:
        result: Dict = {}
        for line in self.soup_text.split():
            list_test: List[str] = self._remove_special_symbols(line)
            for word in list_test:
                word = word.strip(self.special_symbols)
                if word and word not in self.special_symbols:
                    result[word] = result.get(word, 0) + 1
        return result

    def _remove_special_symbols(self, line: str) -> List[str]:
        result: List[str] = [line]
        for special_symbol in self.special_symbols:
            tmp_list: List[str] = []
            for _list in result:
                tmp_list += _list.split(special_symbol)
            result = tmp_list[:]
        return result
