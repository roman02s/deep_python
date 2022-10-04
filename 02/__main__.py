from parse_json import parse_json


def callback(required_field: str, keyword: str):
    """Заглушка для выполнения в parse_json"""
    print("keyword_callback сработал для: ", required_field, " ", keyword, "!", sep='')


if __name__ == "__main__":
    str_json: str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(str_json, required_fields=["key1"], keywords=["word2"],
               keyword_callback=callback)
