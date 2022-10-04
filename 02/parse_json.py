import json
from typing import Callable, List


def parse_json(json_str: str,
               required_fields: List[str] = None,
               keywords: List[str] = None,
               keyword_callback: Callable[[str, str], None] = None):
    """Парсинг json строки json_str по списку полей required_fields,
    списку имен keywords и функции-обработчика имени keyword_callback"""
    try:
        json_doc: dict = json.loads(json_str)
    except json.decoder.JSONDecodeError as json_error:
        print("Ошибка парсинга json строки:", json_error)
        return
    for required_field in required_fields:
        if json_doc.get(required_field, ""):
            for keyword in keywords:
                if keyword in json_doc.get(required_field, ""):
                    keyword_callback(required_field, keyword)
