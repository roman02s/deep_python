
class Response:
    status = 200

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def read():
        return b"test data"


class AioHttpBase:
    class ClientSession:
        def __init__(self):
            pass

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        @staticmethod
        def get(url):
            return Response()
