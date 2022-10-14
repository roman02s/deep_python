import pytest

from CustomMeta.CustomMeta import CustomMeta


def test_example():
    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        @staticmethod
        def line():
            return 100

        def __str__(self):
            return "Custom_by_metaclass"

    inst = CustomClass()
    assert inst.custom_x == 50
    assert inst.custom_val == 99
    assert inst.custom_line() == 100
    assert CustomClass.custom_x == 50
    assert str(inst) == "Custom_by_metaclass"
    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
    with pytest.raises(AttributeError) as exc_info:
        inst.dynamic
    assert isinstance(exc_info.value, AttributeError)

    with pytest.raises(AttributeError) as exc_info:
        inst.x
    assert isinstance(exc_info.value, AttributeError)

    with pytest.raises(AttributeError) as exc_info:
        inst.val
    assert isinstance(exc_info.value, AttributeError)

    with pytest.raises(AttributeError) as exc_info:
        inst.line()
    assert isinstance(exc_info.value, AttributeError)

    with pytest.raises(AttributeError) as exc_info:
        inst.yyy
    assert isinstance(exc_info.value, AttributeError)


def test_append_attribute():
    class CustomClass(metaclass=CustomMeta):
        pass

    cls = CustomClass()
    cls.value: int = 10
    assert cls.custom_value == 10
    with pytest.raises(AttributeError) as exc_info:
        cls.value
    assert isinstance(exc_info.value, AttributeError)


def test_exist_attribute():
    class CustomClass(metaclass=CustomMeta):
        x: int = 123

    assert CustomClass.custom_x == 123


@pytest.mark.parametrize("mapping", [
    lambda name: f"new_mapping_{name}",
    lambda name: name,
])
def test_mapping(mapping):
    class CustomClass(metaclass=CustomMeta.mapping(mapping)):
        x: int = 123

    assert CustomClass.__dict__[mapping("x")] == 123
