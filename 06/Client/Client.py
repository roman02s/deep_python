import socket


class ClientError(Exception):
    def __init__(self, error: str):
        print(f"ClientError: {error}")


class Client:
    __bufsize_message = 1024
    __sep = '\n'

    def __init__(self, host: str, port: int, timeout: int = None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError(f"Cannot create connection - {err}")

    def read(self):

        data: bytes = b""
        while not data.endswith(self.__sep.encode()):
            try:
                data += self.connection.recv(self.__bufsize_message)
            except socket.error as err:
                raise ClientError(f"Error reading data from socket - {err}")

        return data.decode('utf-8')

    def send(self, data: str):
        try:
            self.connection.sendall(str(data + self.__sep).encode())
        except socket.error as err:
            raise ClientError(f"Error sending data from socket - {err}")

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError(f"Error. Do not close the connection - {err}")

