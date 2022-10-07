from copy import deepcopy
from functools import reduce
from typing import Tuple, Union, List

TypeList = Union[List, "CustomList"]


class CustomList(list):
    """Пользовательский класс, отнаследованный от списка"""

    def _get_both_list(self, other: TypeList) -> Tuple["CustomList", TypeList]:
        copy_self = deepcopy(self)
        copy_other = deepcopy(other)
        length_diff = len(self) - len(other)
        padding = (0 for _ in range(abs(length_diff)))

        if length_diff < 0:
            copy_self.extend(padding)
        if length_diff > 0:
            copy_other.extend(padding)
        return copy_self, copy_other

    @staticmethod
    def _sum(list_instance: TypeList) -> int:
        return reduce(lambda x, y: x + y, list_instance, 0)

    def __add__(self, other: TypeList) -> "CustomList":
        copy_self, copy_other = self._get_both_list(other)
        return CustomList([x + y for x, y in zip(copy_self, copy_other)])

    def __sub__(self, other: TypeList) -> "CustomList":
        copy_self, copy_other = self._get_both_list(other)
        return CustomList([x - y for x, y in zip(copy_self, copy_other)])

    def __rsub__(self, other: TypeList) -> "CustomList":
        copy_self, copy_other = self._get_both_list(other)
        return CustomList([x - y for x, y in zip(copy_other, copy_self)])

    def __radd__(self, other: TypeList) -> "CustomList":
        return self.__add__(other)

    def __str__(self) -> str:
        return super(CustomList, self).__str__() + ", " + f"sum: {self._sum(self)}"

    def __le__(self, other: TypeList) -> bool:
        return self._sum(self) <= self._sum(other)

    def __lt__(self, other: TypeList) -> bool:
        return self._sum(self) < self._sum(other)

    def __ge__(self, other: TypeList) -> bool:
        return self._sum(self) >= self._sum(other)

    def __gt__(self, other: TypeList) -> bool:
        return self._sum(self) > self._sum(other)

    def __eq__(self, other: TypeList) -> bool:
        return self._sum(self) == self._sum(other)

    def __ne__(self, other: TypeList) -> bool:
        return self._sum(self) != self._sum(other)
