import socket


class ClientError(Exception):
    def __init__(self, error: str):
        print(f"ClientError: {error}")


class Client:
    BUFSIZE = 1024

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError(f"Cannot create connection - {err}")

    def read(self):

        data = b""

        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(self.BUFSIZE)
            except socket.error as err:
                raise ClientError(f"Error reading data from socket - {err}")

        return data.decode('utf-8')

    def send(self, data):
        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise ClientError(f"Error sending data from socket - {err}")

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError(f"Error. Do not close the connection - {err}")


