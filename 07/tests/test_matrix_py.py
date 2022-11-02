import random
import pytest

from Matrix.python.Matrix import Matrix


@pytest.fixture(scope="function")
def matrix_1() -> Matrix:
    return Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])


@pytest.fixture(scope="function")
def matrix_2() -> Matrix:
    return Matrix([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ])


@pytest.fixture(scope="function")
def result_matrix_mul() -> Matrix:
    return Matrix([
        [300, 360, 420],
        [660, 810, 960],
        [1020, 1260, 1500],
    ])


@pytest.mark.parametrize("row, column", [
    (random.randint(1, 10), random.randint(1, 10)) for _ in range(10)
])
def test_matrix_size(row, column):
    input_list = [[0 for _ in range(column)] for _ in range(row)]
    matrix = Matrix(input_list)
    assert matrix.size() == (row, column)


def test_matrix_mul_success(matrix_1, matrix_2, result_matrix_mul):
    assert matrix_1 * matrix_2 == result_matrix_mul


def test_matrix_mul_error_dim(matrix_1):
    error_matrix = Matrix([[1, 2, 3]])
    assert not matrix_1 * error_matrix


def test_matrix_get_set_item(matrix_1):
    matrix_1[0] = [3, 4, 5]
    assert matrix_1[0] == [3, 4, 5]


def test_matrix_to_list(matrix_1):
    assert matrix_1.to_list() == matrix_1._matrix

