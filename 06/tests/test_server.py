import pytest

from Server.Server import Server


def test_server_base():
    Server.worker_processing = lambda _str: "Test processing data"
    Server.data_send = lambda _str: "send response"
    Server._buffer = b"\n"
    Server.data_received(Server, b"some get data\n")


def test_server_error_get_data():
    Server.worker_processing = lambda _str: "Test processing data"
    Server.data_send = lambda _str: "send response"
    Server._buffer = "\n"

    with pytest.raises(TypeError) as exc_info:
        Server.data_received(Server, b"some get data\n")
    assert isinstance(exc_info.value, TypeError)
