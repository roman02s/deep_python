import asyncio
from collections import defaultdict
from copy import deepcopy


class StorageDriverError(ValueError):
    pass


class Storage:
    """Класс для хранения метрик в памяти процесса"""

    def __init__(self):
        self._data = defaultdict(dict)

    def put(self, key, value, timestamp):
        self._data[key][timestamp] = value

    def get(self, key):

        if key == '*':
            return deepcopy(self._data)

        if key in self._data:
            return {key: deepcopy(self._data.get(key))}

        return {}


class StorageDriver:
    """Класс, предосталяющий интерфейс для работы с хранилищем данных"""

    def __init__(self, storage: Storage):
        self.storage = storage

    def __call__(self, data: str):

        method, *params = data.split()

        if method == "put":
            key, value, timestamp = params
            value, timestamp = float(value), int(timestamp)
            self.storage.put(key, value, timestamp)
            return {}
        elif method == "get":
            key = params.pop()
            if params:
                raise StorageDriverError
            return self.storage.get(key)
        else:
            raise StorageDriverError


class Server(asyncio.Protocol):
    # настройки сообщений сервера
    sep = '\n'
    error_message = "wrong command"
    code_err = 'error'
    code_ok = 'ok'

    def __init__(self):
        super().__init__()
        self._buffer: bytes = b""

    def connection_made_write(self, transport: asyncio.transports.BaseTransport) -> None:
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        """Метод data_received вызывается при получении данных в сокете"""
        self._buffer += data

        try:
            request = self._buffer.decode()
            # ждем данных, если команда не завершена символом sep
            if not request.endswith(self.sep):
                return

            self._buffer, message = b"", ""
            # Обработка сообщения здесь

            code = self.code_ok
        except (ValueError, UnicodeDecodeError, IndexError):
            message = self.error_message + self.sep
            code = self.code_err

        response = f'{code}{self.sep}{message}{self.sep}'
        # отправляем ответ
        if hasattr(self.transport, "write"):
            self.transport.write(response.encode())
        

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(Server, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
