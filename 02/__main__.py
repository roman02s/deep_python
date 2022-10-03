import json
from parse_json import parse_json


if __name__ == "__main__":
    str_json = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(str_json, required_fields=["key1"], keywords=["word2"], keyword_callback=lambda rf, kw: print("keyword_callback сработал для: ", rf, " ", kw, "!", sep=''))
    pass
