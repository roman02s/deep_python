from typing import Optional
import asyncio

from Worker.Worker import Worker


class Server(asyncio.Protocol):
    # настройки сообщений сервера
    sep = '\n'
    error_message = "wrong command"
    code_err = 'error'
    code_ok = 'ok'

    def __init__(self):
        super().__init__()
        self._buffer: bytes = b""

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
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
            worker = Worker(request[:-1])
            message = worker.fetch_url()
            code = self.code_ok
        except (ValueError, UnicodeDecodeError, IndexError):
            message = self.error_message + self.sep
            code = self.code_err
        response = f'{code}{self.sep}{message}{self.sep}'
        print(f"{response=}")
        # отправляем ответ
        if hasattr(self.transport, "write"):
            self.transport.write(str(response + self.sep).encode())

    @staticmethod
    def worker_processing(url: str) -> Optional[str]:
        worker = Worker(url)
        return worker.fetch_url()
        

def run_server(host: str, port: int):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(Server, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("KeyboardInterrupt in run_server")

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
