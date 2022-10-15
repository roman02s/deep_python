import io
from typing import IO, List

import pytest

from filter_file import filter_file


@pytest.fixture
def file_text() -> str:
    return "а Роза упала на лапу Азора"


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
    assert filter_file(file, word_list) == [file_text]


def test_error(file, error_word_list):
    assert not filter_file(file, error_word_list)


def test_empty_word_list(file):
    empty_word_list = []
    assert not filter_file(file, empty_word_list)


def test_empty_file(word_list):
    empty_file = io.StringIO(initial_value="", newline="\n")
    assert not filter_file(empty_file, word_list)
