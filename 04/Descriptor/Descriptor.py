def type_hint(expected_type):
    def hint(value):
        if isinstance(value, expected_type):
            return
        raise TypeError("Invalid type")
    return hint


def make_descriptor(expected_type: type):
    def make_type_hint(_expected_type: type):
        def hint(_, value):
            if isinstance(value, _expected_type):
                return
            raise TypeError("Invalid type")

        return hint

    class Descriptor:
        __value: expected_type
        __type_hint = make_type_hint(expected_type)

        def __init__(self, default_value=expected_type()):
            self.__type_hint(default_value)
            self.__value = default_value

        def __get__(self, instance, owner):
            return self.__value

        def __set__(self, instance, value):
            self.__type_hint(value)
            self.__value = value

    return Descriptor


class String(make_descriptor(str)):
    pass


class Integer(make_descriptor(int)):
    pass


class PositiveInteger(Integer):
    def __init__(self, value=int()):
        PositiveInteger.__value_hint(value)
        super().__init__(value)

    def __set__(self, instance, value):
        PositiveInteger.__value_hint(value)
        super().__set__(instance, value)

    @staticmethod
    def __value_hint(value):
        if value >= 0:
            return
        raise ValueError("Integer not positive")
