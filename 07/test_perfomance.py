#! /usr/bin/env python
import time
import random
from typing import List
from Matrix.python.Matrix import Matrix as Matrix_py

from Matrix.cython import Matrix


def generate_matrix(row: int, column: int, seed: int = 0) -> List:
    random.seed(seed)
    return [[random.randint(1, 11) for _ in range(column)] for _ in range(row)]


N, M, K = 500, 500, 500


def matrix_1() -> List[List]:
    return generate_matrix(N, M, 0)


def matrix_2() -> List[List]:
    return generate_matrix(M, K, 0)


start_ts = time.time()
res_python = Matrix_py(matrix_1()) * Matrix_py(matrix_2())
end_ts = time.time()
print(f"Time of execution of python matrix_mul is {end_ts - start_ts} seconds")
res_python = res_python.to_list()

start_ts = time.time()
res_cython = Matrix.matrix_mul(matrix_1(), matrix_2())
end_ts = time.time()
print(f"Time of execution of cython matrix_mul is {end_ts - start_ts} seconds")
assert res_cython == res_python
