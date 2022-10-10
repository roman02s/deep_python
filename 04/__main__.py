from CustomMeta.CustomMeta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def some_def_1(self):
        print(f"{type(self).__name__} call some_def_1")

    def some_def_2(self):
        print(f"{type(self).__name__} call some_def_2")


if __name__ == "__main__":
    CustomClass().some_def_1()
    CustomClass().some_def_2()
