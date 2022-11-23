import random
import pytest

from CustomList.CustomList import CustomList


@pytest.fixture
def some_list_1():
    return [*range(0, 11, 2)]


@pytest.fixture
def some_list_2():
    return [*range(10, 21, 2)]


def test_custom_list_add(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 + custom_list_2
    assert result_custom_list ==\
           CustomList([x + y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_subtraction(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 - custom_list_2
    assert result_custom_list ==\
           CustomList([x - y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_lt(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 < custom_list_2
    assert result_custom_list
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_le(some_list_1, some_list_2):
    _some_list = [1, 2, 3]
    some_list_1 += _some_list
    some_list_2 += _some_list
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 <= custom_list_2
    assert result_custom_list
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_gt(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 > custom_list_2
    assert not result_custom_list
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_ge(some_list_1, some_list_2):
    _some_list = [1, 2, 3]
    some_list_1 += _some_list
    some_list_2 += _some_list
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 >= custom_list_2
    assert not result_custom_list
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_eq(some_list_1):
    assert CustomList(some_list_1) == CustomList(some_list_1)


def test_custom_list_nq(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 != custom_list_2
    assert result_custom_list
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_rsub(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = list(custom_list_1) - custom_list_2
    assert result_custom_list ==\
           CustomList([x - y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_radd(some_list_1, some_list_2):
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = list(custom_list_1) + custom_list_2
    assert result_custom_list ==\
           CustomList([x + y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_get_both_list_extend_1(some_list_1):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    custom_list_1 = CustomList(some_list_1)
    result_custom_lists =\
        custom_list_1._get_both_list(some_list_1 + [1, 2, 3])
    assert result_custom_lists ==\
           (CustomList(some_list_1 + [0, 0, 0]), list(some_list_1 + [1, 2, 3]))
    assert custom_list_1 == CustomList(some_list_1)


def test_custom_list_get_both_list_extend_2(some_list_1):
    """Тест, проверяющий расширение 2-го списка до длины первого"""
    custom_list_1 = CustomList(some_list_1 + [1, 2, 3])
    result_custom_lists =\
        custom_list_1._get_both_list(some_list_1)
    assert result_custom_lists ==\
           (CustomList(some_list_1 + [1, 2, 3]), list(some_list_1 + [0, 0, 0]))
    assert custom_list_1 == CustomList(some_list_1 + [1, 2, 3])


def test_custom_list_extend_1_list_add(some_list_1, some_list_2):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    some_list_1 = some_list_1[:] + [1, 2, 3]
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 + custom_list_2
    assert result_custom_list == \
           CustomList([x + y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_extend_1_list_sub(some_list_1, some_list_2):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    some_list_1 = some_list_1[:] + [1, 2, 3]
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 - custom_list_2
    assert result_custom_list == \
           CustomList([x - y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_extend_2_list_add(some_list_1, some_list_2):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    some_list_2 = some_list_2[:] + [1, 2, 3]
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 + custom_list_2
    assert result_custom_list == \
           CustomList([x + y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)


def test_custom_list_extend_2_list_sub(some_list_1, some_list_2):
    """Тест, проверяющий расширение 1-го списка до длины второго"""
    some_list_2 = some_list_2[:] + [1, 2, 3]
    custom_list_1 = CustomList(some_list_1)
    custom_list_2 = CustomList(some_list_2)
    result_custom_list = custom_list_1 - custom_list_2
    assert result_custom_list == \
           CustomList([x - y for x, y in zip(some_list_1, some_list_2)])
    assert custom_list_1 == CustomList(some_list_1)
    assert custom_list_2 == CustomList(some_list_2)
