import pytest

from Descriptor.Descriptor import (
    Integer,
    String,
    PositiveInteger,
    type_hint,
    make_descriptor,
)


@pytest.fixture
def types():
    """Integer, String, PositiveInteger"""
    return int, str, int


@pytest.fixture
def types_error():
    return list


@pytest.fixture
def positive_int():
    return 10


@pytest.fixture
def negative_int():
    return -10


def test_hint(types, types_error):
    for type_ in types:
        hint = type_hint(type_)
        instance = type_()
        hint(instance)
        another_instance = types_error()
        with pytest.raises(TypeError) as exc_info:
            hint(another_instance)
        assert isinstance(exc_info.value, TypeError)


def test_default_values():
    class Data:
        integer = Integer()
        positive = PositiveInteger()
        string = String()

    data = Data()
    assert isinstance(data.integer, int)
    assert isinstance(data.positive, int)
    assert isinstance(data.string, str)

    assert data.integer == int()
    assert data.positive == int()
    assert data.string == str()


def test_typed_property(types, types_error):
    for type_ in types:
        type_descriptor = make_descriptor(type_)

        class Data:
            data = type_descriptor()

        container = Data()
        assert isinstance(container.data, type_)
        container.data = type_()

        with pytest.raises(TypeError) as exc_info:
            invalid_class_instance = types_error()
            container.data = invalid_class_instance
        assert isinstance(exc_info.value, TypeError)


def test_positive_int(positive_int, negative_int):
    class SampleContainer:
        pos = PositiveInteger(positive_int)

    data = SampleContainer()
    assert isinstance(data.pos, int)
    assert data.pos == positive_int

    with pytest.raises(ValueError) as exc_info:
        data.pos = negative_int
    assert isinstance(exc_info.value, ValueError)

    with pytest.raises(ValueError) as exc_info:
        PositiveInteger(negative_int)
    assert isinstance(exc_info.value, ValueError)


def test_error_data(positive_int, negative_int):
    class Data:
        positive = PositiveInteger(positive_int)
        integer = Integer(negative_int)
        ordinary_string = String("asd")

    data = Data()

    with pytest.raises(TypeError) as exc_info:
        data.positive = "asd"
    assert isinstance(exc_info.value, TypeError)
    assert data.positive == positive_int

    with pytest.raises(ValueError) as exc_info:
        data.positive = negative_int
    assert isinstance(exc_info.value, ValueError)
    assert data.positive == positive_int

    with pytest.raises(TypeError) as exc_info:
        data.integer = "asd"
    assert isinstance(exc_info.value, TypeError)

    with pytest.raises(TypeError) as exc_info:
        data.ordinary_string = 123
    assert isinstance(exc_info.value, TypeError)
