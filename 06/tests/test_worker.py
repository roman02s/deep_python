from bs4 import BeautifulSoup
import pytest

from Worker.Worker import Worker
from static import static_data


def test_parser_url_empty():
    test_worker = Worker()
    assert not test_worker.fetch_url()


@pytest.mark.parametrize("test_file, result_parsing", [
    ("static/test_html_parsing_ru.html", static_data.RESULT_PARSE_HTML_RU),
    ("static/test_html_parsing_en.html", static_data.RESULT_PARSE_HTML_EN),
])
def test_parser_url(test_file, result_parsing):
    test_worker = Worker()
    with open(test_file, "r", encoding="utf-8") as file:
        html = file.read()
        soup = BeautifulSoup(html, "html5lib")
        test_worker.soup_text = soup.text
    assert result_parsing == test_worker.fetch_url()
