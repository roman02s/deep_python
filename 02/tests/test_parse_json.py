"""
Юнит-тесты функции parse_json.
"""
import pytest
from json_factory.json_factory import JSONFactory
from parse_json import parse_json


def keyword_callback_mock(count: list):
    """Mock-объект для выполнения тестирования parse_json"""

    def mock_func(required_field: str, keyword: str):
        nonlocal count
        count.append(count.pop() + 1)
    return mock_func


def test_parse_json_main():
    """Реализация случая из задания"""
    count: 'list[int]' = [0]
    str_json: str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(str_json, required_fields=["key1"], keywords=["word2"],
               keyword_callback=keyword_callback_mock(count))
    assert count[0] == 1


@pytest.mark.parametrize("len_keywords",  list(range(1, 10)))
def test_parse_json_count_keyword_callback(len_keywords: int):
    """Тест, проверяющий корректность работы parse_json по keyword"""
    count: 'list[int]' = [0]
    str_json: str = JSONFactory.generate([1, len_keywords])
    parse_json(str_json, required_fields=JSONFactory.get_fields(),
               keywords=JSONFactory.get_keywords(), keyword_callback=keyword_callback_mock(count))
    assert count[0] == len_keywords


@pytest.mark.parametrize("len_fields", list(range(1, 10)))
def test_parse_json_count_field_callback(len_fields: int):
    """Тест, проверяющий корректность работы parse_json по field"""
    count: 'list[int]' = [0]
    str_json: str = JSONFactory.generate([len_fields, 1])
    parse_json(str_json, required_fields=JSONFactory.get_fields(),
               keywords=JSONFactory.get_keywords(), keyword_callback=keyword_callback_mock(count))
    assert count[0] == len_fields

def test_parse_json_fail():
    """Тест, при котором подается ошибочная json строка"""
    count: 'list[int]' = [0]
    str_json: str = JSONFactory.generate([1, 1])
    error_str: str = "}{asdasd"
    parse_json(error_str, required_fields=JSONFactory.get_fields(),
               keywords=JSONFactory.get_keywords(), keyword_callback=keyword_callback_mock(count))
    assert count[0] == 0