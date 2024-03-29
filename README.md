# Практические задания по курсу "Углубленный Python"

**Сим Роман Дмитриевич**
<details>
<summary>Домашнее задание №1</summary>

### 1. Написать консольную игру крестики-нолики.

Пример того, как схематично можно изобразить класс игры.

```py
class TicTacGame:

    def show_board():
        pass

    def validate_input():
        pass

    def start_game():
        pass

    def check_winner():
        pass


if __name__ == "__main__":
    game = TicTac()
    game.start_game()

```
Допустима реалиция без использоавния классов.

Пользовательский ввод осуществляется с помощью input, который необходимо валидировать и выводить понятное описание ошибки.

Схема класса не обязательно должна быть такой, можно добавлять и менять методы, держа в голове грамотную организацию кода, ненужное дублирование и код-лапшу.

По желанию, можно написать вспомогательную функцию, запустив которую, компьютер сыграет сам с собой без участия человека, либо сделать возможным игру между человеком и компьютером.


### 2. Написать тесты (unittest, assert) для игры, покрыв тестами основные методы

### 3. Проверить корректность и стиль кода с помощью pylint или flake8

### 3. Проверить покрытие тестов через coverage

</details>


<details>
<summary>Домашнее задание №2</summary>

### Написать функцию, которая в качестве аргументов принимает строку json, список полей, которые необходимо обработать, список имён, которые нужно найти и функцию-обработчика имени, который срабатывает, когда в каком-либо поле было найдено ключевое имя.

Функция, должна принимать строку, в которой содержится json, и произвести парсинг этого json.
Упростим немного и представим, что json представляет из себя только коллекцию ключей-значений.
Причём ключами и значениями являются только строки.

```py
def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback)
```

Например, представим, что json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}', а required_fields = ["key1"], keywords = ["word2"]. Тогда keyword_callback будет вызвана только для слова 'word2' для ключа 'key1'.

Распарсить json можно так:
```py
import json

...
json_doc = json.loads(json_str)

```

Можно использовать ещё ujson, но его предварительно нужно установить с помощью pip.

### Использовать mock-объект при тестировании
Использовать mock-объект, например, keyword_callback и проверить, что заглушка вызывалась n число раз.

### Использовать factory boy
Для генерации данных и ключевых слов, нужно использовать factory boy.

### Узнать степень покрытия тестами с помощью библиотеки coverage

</details>

<details>
<summary>Домашнее задание №3 (объектная модель, ООП)</summary>

### Реализовать класс, отнаследованный от списка

При этом один список:
- Можно вычитать из другого CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]) = CustomList([4, -1, -4, 7]);
- Можно складывать с другим CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]) = CustomList([6, 3, 10, 7]);
- Результатом сложения/вычитания должен быть новый кастомный список;
- Сложение/вычитание также должно работать с обычными списками:<br>
    [1, 2] +- CustomList([3, 4]) -> CustomList(...)<br>
    CustomList([3, 4]) +- [1, 2] -> CustomList(...)
- При неравной длине, дополнять меньший список нулями только на время выполнения операции. Исходные списки не должны изменяться;
- При сравнении списков должна сравниваться сумма элементов списков;
- Должен быть переопределен str, чтобы выводились элементы списка и их сумма;
- Списки можно считать всегда числовыми;
- На все должны быть тесты в отдельном модуле;
- Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black.

</details>


<details>
<summary>Домашнее задание №4 (дескрипторы, метаклассы)</summary>

### 1. Написать метакласс, который в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_" (+тесты).
  Подменяться должны так же атрибуты экземпляра после создания экземпляра класса (dynamic в примере).

```py
    class CustomMeta():
        pass

    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"

    inst = CustomClass()
    inst.custom_x == 50
    inst.custom_val == 99
    inst.custom_line() == 100
    CustomClass.custom_x == 50
    str(inst) == "Custom_by_metaclass"

    inst.dynamic = "added later"
    inst.custom_dynamic == "added later"
    inst.dynamic  # ошибка

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка
    CustomClass.x  # ошибка
```


### 2. Дескрипторы с проверками типов и значений данных (+тесты)

```py
    class Integer:
        pass

    class String:
        pass

    class PositiveInteger:
        pass

    class Data:
        num = Integer()
        name = String()
        price = PositiveInteger()

        def __init__(...):
            ....
```


### 3. Тесты в отдельном модуле

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

</details>

<details>
<summary> Домашнее задание №5 (стандартная библиотека)</summary>

## 1. LRU-кэш
Интерфейс:

```py
    class LRUCache:

        def __init__(self, limit=42):
            pass

        def get(self, key):
            pass

        def set(self, key, value):
            pass


    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"


    Если удобнее, get/set можно сделать по аналогии с dict:
    cache["k1"] = "val1"
    print(cache["k3"])
```

Реализация любым способом без исспользования OrderedDict.

### 2. Написать генератор filter_file для чтения и фильтрации файла
Есть текстовый файл, который может не помещаться в память.
В каждой строке файла фраза или предложение: набор слов, разделенных пробелами (знаков препинания нет).

Генератор должен принимать на вход имя файла или файловый объект и список слов для поиска.
Генератор перебирает строки файла и возвращает только те из них (строку целиком), где встретилось хотя бы одно из слов для поиска.
Поиск должен выполняться по полному совпадению слова без учета регистра.

Например, для строки из файла "а Роза упала на лапу Азора" слово поиска "роза" должно сработать, а "роз" или "розан" - уже нет.

Для тестов можноо в том числе использовать StringIO.

### 3. Тесты в отдельном модуле

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

</details>


<details>
<summary> Домашнее задание №6 (потоки, процессы) </summary>

### 1. Клиент-серверное приложение для обкачки набора урлов
#### Cервер
master-worker cервер для обработки запросов от клиента.

Алгоритм должен быть следующим:

    - Мастер и воркеры это разные потоки в едином приложении;
    - Количество воркеров задается при запуске;
    - Мастер слушает порт, на который клиент будет по TCP отправлять урлы для обкачки;
    - Мастер принимает запрос, читает url от клиента и передаёт этот url одному из воркеров;
    - Воркер обкачивает url по https и возвращает клиенту топ K самых частых слов и их частоту в формате json {"word1": 10, "word2": 5};
    - После каждого обработанного урла сервер должен вывести статистику: сколько урлов было обработано на данный момент суммарно всеми воркерами;

`python server.py -w 10 -k 7` (сервер использует 10 воркеров для обкачки и отправляет клиенту топ-7 частых слов)

#### Клиент
Утилита, отправляющая запросы с урлами серверу по TCP в несколько потоков.
Нужно сделать следующее:

    - Подготовить файл с запросами (порядка 100 разных url);
    - На вход клиенту передаётся два аргумента --- файл с URL'ами и M (количество потоков);
    - Клиент создает M потоков, отправляет запросы на сервер в каждом потоке и печатает ответ сервера в стандартый вывод, например: `xxx.com: {'word1': 100, 'word2': 50}`.

`python client.py 10 urls.txt`


Все действия должны быть выделены в классы/функции.

### 2. Тесты в отдельном модуле

### 3. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
</details>

<details>
<summary> Домашнее задание №7</summary>

### 1. Реализовать умножение цепочки матриц на С и сравнить производительность кода на C и на Python.
</details>

<details>
<summary> Домашнее задание №8 </summary>

### 1. Скрипт для асинхронной обкачки урлов
Написать скрипт для обкачки списка урлов с возможностью задавать количество одновременных запросов, используя асинхронное программирование.
Клиент можно использовать любой, например, из aiohttp.
Так, 10 одновременных запросов могут задаваться командой:

`python fetcher.py -c 10 urls.txt`
или
`python fetcher.py 10 urls.txt`

### 2. Тесты в отдельном модуле

### 3. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

</details>

<details>

<summary> Домашнее задание №9</summary>

### 1. Сравнение использования weakref и слотов
Нужно придумать свои типы с несколькими атрибутами:
- класс с обычными атрибутами
- класс со слотами
- класс с атрибутами weakref

Для каждого класса создается большое число экземпляров и замеряется (сравнивается):
- время создания пачки экземпляров
- время доступа/изменения/удаления атрибутов

Результаты оформляются скриншотами c описанием.

### 2. Профилирование
Провести профилирование вызовов и памяти для кода из пункта 1.

Результаты оформляются скриншотами c описанием.

### 3. Декоратор для профилирования
Применение декоратора к функции должно выполнять прoфилироование всех запусков данной функции.
Вызов метода `.print_stat()` должен выводить статистику прифилирования.


```py
def profile_deco():
    ...


@profile_deco
def add(a, b):
    return a + b

@profile_deco
def sub(a, b):
    return a - b

add(1, 2)
add(4, 5)

add.print_stat()  # выводится таблица с результатами профилирования
```

### 4. Тесты не нужны

### 5. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black



</details>