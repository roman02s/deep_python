import io
from typing import IO, List

import pytest

from filter_file import filter_file


@pytest.fixture
def file_text() -> str:
    return "а Роза упала на лапу Азора\n"


@pytest.fixture
def word_list() -> List[str]:
    return ["роза"]


@pytest.fixture
def error_word_list() -> List[str]:
    return ["роз", "розан"]


@pytest.fixture
def file(file_text: str) -> IO:
    fp = io.StringIO(initial_value=file_text, newline="\n")
    return fp


def test_success(file, file_text, word_list):
    res_list = []
    for word in filter_file(file, word_list):
        res_list.append(word)
    print(res_list, [file_text])
    assert res_list == [file_text]


def test_error(file, error_word_list):
    res_list = []
    for word in filter_file(file, error_word_list):
        res_list.append(word)
    assert res_list == []


def test_empty_word_list(file):
    res_list = []
    empty_word_list = []
    for word in filter_file(file, empty_word_list):
        res_list.append(word)
    assert res_list == []


def test_empty_file(word_list):
    res_list = []
    empty_file = io.StringIO(initial_value="", newline="\n")
    for word in filter_file(empty_file, word_list):
        res_list.append(word)
    assert res_list == []


def test_several_times():
    file = io.StringIO(initial_value="омар\nамур\nаром\nурам\nомар\nомар\n", newline="\n")
    res_list = []
    word_list = ["омар"]
    file_text_list = ["омар\n", "омар\n", "омар\n"]
    for word in filter_file(file, word_list):
        res_list.append(word)
    assert res_list == file_text_list
