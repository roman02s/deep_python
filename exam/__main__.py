# 1) Типы данных в Python, изменяемые/неизменяемые, сложности основных операций контейнерных типов.
# 2) Потоки, GIL, особенности использования потоков для различных задач.
# 3) Написать декоратор, который считает и выводит среднее время выполнения последних k вызовов исходной функции.
# k задается через параметр декоратора.
# После каждого вызова задекорированной функции должно выводиться среднее по k последним вызовам.
import time


def mean_deco(k):
    def func(input_func):
        def wrap(*args, **kwargs):
            wrap.__dict__["list_time"] = wrap.__dict__.get("list_time", [])
            start_time = time.time()
            result = input_func(*args, **kwargs)
            end_time = time.time()
            if len(wrap.list_time) >= k:
                wrap.list_time = wrap.list_time[1:]
            wrap.list_time.append(end_time - start_time)
            print(sum(wrap.list_time) / k)
            return result
        return wrap
    return func


@mean_deco(10)
def foo(arg1):
    [0 for _ in range(1000000)]
    return 10


@mean_deco(2)
def boo(a, b):
    [0 for _ in range(1000)]
    return a + b


for _ in range(15):
    foo("Walter") # при каждом вызове выводится среднее по k=10 последним вызовам
    boo(12, 13)
    print("==========")
