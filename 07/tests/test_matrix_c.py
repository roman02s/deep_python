import pytest
from typing import List

from Matrix.cython import Matrix


@pytest.fixture(scope="function")
def matrix_1() -> List[List]:
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


@pytest.fixture(scope="function")
def matrix_2() -> List[List]:
    return [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ]


@pytest.fixture(scope="function")
def result_matrix(matrix_1, matrix_2) -> List[List]:
    return [
        [300, 360, 420],
        [660, 810, 960],
        [1020, 1260, 1500],
    ]


def test_matrix_mul_success(matrix_1, matrix_2, result_matrix):
    res_cython = Matrix.matrix_mul(matrix_1, matrix_2)
    assert res_cython == result_matrix
