from typing import List, Tuple, Optional
from copy import deepcopy


class Matrix:

    def __init__(self, input_list: List[List]) -> None:
        self._matrix = deepcopy(input_list)

    def __getitem__(self, item):
        return self._matrix[item]

    def __setitem__(self, key, value) -> None:
        self._matrix[key] = value

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self._matrix)

    def size(self) -> Tuple[int, int]:
        return len(self._matrix), len(self._matrix[0])

    def __mul__(self, other: "Matrix") -> Optional["Matrix"]:
        if self.size()[1] != other.size()[0]:
            print("Нельзя перемножить матрицы таких размерностей")
            return None
        result = []
        for i in range(self.size()[0]):
            res_ = []
            for j in range(other.size()[1]):
                element = 0
                for k in range(min(other.size()[1], len(self._matrix[i]))):
                    element += self._matrix[i][k] * other._matrix[k][j]
                res_.append(element)
            result.append(res_)
        return Matrix(result)

    def __eq__(self, other: "Matrix") -> bool:
        if self._matrix == other._matrix:
            return True
        return False

    def to_list(self) -> List[List]:
        return self._matrix
