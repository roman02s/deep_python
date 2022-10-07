import random
import pytest

from CustomList.CustomList import CustomList


@pytest.fixture
def some_list_1(start: int = 0, end: int = 10, count: int = 5):
    return random.sample(list(range(start, end)), k=count)


@pytest.fixture
def some_list_2(start: int = 10, end: int = 20, count: int = 5):
    return random.sample(list(range(start, end)), k=count)


def test_custom_list_add(some_list_1, some_list_2):
    result_custom_list = CustomList(some_list_1) + CustomList(some_list_2)
    assert result_custom_list == CustomList([x + y for x, y in zip(some_list_1, some_list_2)])


def test_custom_list_subtraction(some_list_1, some_list_2):
    result_custom_list = CustomList(some_list_1) - CustomList(some_list_2)
    assert result_custom_list == CustomList([x - y for x, y in zip(some_list_1, some_list_2)])


def test_custom_list_lt(some_list_1, some_list_2):
    result_custom_list = CustomList(some_list_1) < CustomList(some_list_2)
    assert result_custom_list


def test_custom_list_le(some_list_1, some_list_2):
    result_custom_list = CustomList([1, 2, 3] + some_list_1) <= CustomList([1, 2, 3] + some_list_2)
    assert result_custom_list


def test_custom_list_gt(some_list_1, some_list_2):
    result_custom_list = CustomList(some_list_2) > CustomList(some_list_1)
    assert result_custom_list


def test_custom_list_ge(some_list_1, some_list_2):
    result_custom_list = CustomList([1, 2, 3] + some_list_2) >= CustomList([1, 2, 3] + some_list_1)
    assert result_custom_list


def test_custom_list_eq(some_list_1):
    result_custom_list = CustomList([1, 2, 3] + some_list_1) == CustomList([1, 2, 3] + some_list_1)
    assert result_custom_list


def test_custom_list_nq(some_list_1, some_list_2):
    result_custom_list = CustomList(some_list_1) != CustomList(some_list_2)
    assert result_custom_list


def test_custom_list_rsub(some_list_1, some_list_2):
    result_custom_list = list(some_list_1) - CustomList(some_list_2)
    assert result_custom_list == CustomList([x - y for x, y in zip(some_list_1, some_list_2)])


def test_custom_list_radd(some_list_1, some_list_2):
    result_custom_list = list(some_list_1) + CustomList(some_list_2)
    assert result_custom_list == CustomList([x + y for x, y in zip(some_list_1, some_list_2)])


def test_custom_list_get_both_list_extend_1(some_list_1):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    result_custom_lists = CustomList(some_list_1)._get_both_list(some_list_1 + [1, 2, 3])
    assert result_custom_lists == (CustomList(some_list_1 + [0, 0, 0]), list(some_list_1 + [1, 2, 3]))


def test_custom_list_get_both_list_extend_2(some_list_1):
    """Тест, проверяющий расширение 2-го списка до длины первого"""
    result_custom_lists = CustomList(some_list_1 + [1, 2, 3])._get_both_list(some_list_1)
    assert result_custom_lists == (CustomList(some_list_1 + [1, 2, 3]), list(some_list_1 + [0, 0, 0]))
