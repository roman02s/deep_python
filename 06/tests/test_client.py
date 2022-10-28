from Client.Client import Client


class TestConnection:
    @staticmethod
    def recv(buff_size: int) -> bytes:
        return b"test data recv\n"

    @staticmethod
    def sendall(data: bytes) -> None:
        pass

    @staticmethod
    def close() -> None:
        pass


def test_client_base_read():
    Client.connection = TestConnection()
    assert Client.read(Client) == "test data recv\n"


def test_client_base_send():
    Client.connection = TestConnection()
    Client.send(Client, "some data\n")


def test_client_base_close():
    Client.connection = TestConnection()
    # Some logic with client
    Client.close(Client)
