from  Server.Server import run_server
from Worker.Worker import Worker

if __name__ == "__main__":
    Worker("https://ru.wikipedia.org/wiki/Python").fetch_url()
    # run_server("127.0.0.1", 8888)
