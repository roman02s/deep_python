from Worker.Worker import Worker

import pytest

import static.static_data as static_data


@pytest.mark.parametrize("test_file, result_parsing", [
    ("static/test_html_parsing_ru.html", static_data.RESULT_PARSE_HTML_RU),
("static/test_html_parsing_en.html", static_data.RESULT_PARSE_HTML_EN),
])
def test_parser_url(test_file, result_parsing):
    test_worker = Worker()
    with open(test_file, "r") as file:
        test_worker.soup_text = file.read()
    print(test_worker.fetch_url())
    assert result_parsing == test_worker.fetch_url()
