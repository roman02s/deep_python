# 1) Типы данных в Python, изменяемые/неизменяемые, сложности основных операций контейнерных типов.

Неизменяемые

○ int, float, bool, complex

○ str, bytes ○ tuple

○ frozenset

Изменяемые

○ list

○ dict, set

○ user defined


# 2) Потоки, GIL, особенности использования потоков для различных задач.


Thread (поток) - это сущность операционной системы,
процесс выполнения на процессоре набора инструкций, а именно программного кода.

Global Interpreter Lock (GIL) — это способ синхронизации потоков,
который используется в некоторых интерпретируемых языках программирования.

Mutex, который разрешает только одному потоку использовать интерпретатор python


    import threading
    import time
    def thread_function(name):
        time.sleep(2)

    if __name__ == "__main__":
        x = threading.Thread(target=thread_function, args=(1,))
        x.start() # Запуск
        x.join() # Дождаться завершения другого потока (основной ждет х)