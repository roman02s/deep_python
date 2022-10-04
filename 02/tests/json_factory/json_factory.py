import string
import factory


class JSONFactory(factory.Factory):
    """Генератор JSON"""
    fields: list = []
    keywords: list = []

    @classmethod
    def generate(cls, strategy: list, **kwargs) -> str:
        """Метод для генерации json строки с strategy[0] элементов
        и strategy[1] значений для каждого элемента"""
        cls.fields: list = []
        cls.keywords: list = []
        result = "{\n"
        for i in range(strategy[0]):
            result += '  "' + string.ascii_letters[i] + '"' + ": "
            cls.fields.append(string.ascii_letters[i])
            if strategy[1] > 1:
                result += "["
            for j in range(strategy[1]):
                if j > len(string.ascii_uppercase):
                    j = 0
                result += '"' + string.ascii_uppercase[j + i] + '"'
                cls.keywords.append(string.ascii_uppercase[j + i])
                if j != strategy[1] - 1:
                    result += ", "
            if strategy[1] > 1:
                result += "]"
            if i != strategy[0] - 1:
                result += ","
            result += "\n"
        result += "}\n"
        return result

    @classmethod
    def get_fields(cls):
        return cls.fields

    @classmethod
    def get_keywords(cls):
        return cls.keywords
