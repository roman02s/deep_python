from typing import List, Optional, IO


def filter_file(file: IO, word_list: Optional[List[str]]) -> Optional[str]:
    """
    Генератор принимет на вход имя файла или файловый объект и
    список слов для поиска. Генератор перебирает строки файла и
    возвращает только те из них (строку целиком), где встретилось
    хотя бы одно из слов для поиска. Поиск выполняется по полному
    совпадению слова без учета регистра.
    """
    if word_list is None:
        return
    for line in file:
        line_list = line.split()
        for word in word_list:
            for _line_unit in line_list:
                if word.lower() == _line_unit.lower():
                    yield line
