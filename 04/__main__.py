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
    CustomClass(12).custom_some_def_1()
    inst = CustomClass()
    print(inst.custom_x == 50)
    print(inst.custom_val == 99)
    print(inst.custom_line() == 100)
    print(CustomClass.custom_x == 50)
    print(str(inst) == "Custom_by_metaclass")
    inst.dynamic = "added later"
    print(inst.custom_dynamic == "added later")
    try:
        inst.dynamic  # ошибка
        print("False")
    except AttributeError:
        print("True")

    try:
        inst.x  # ошибка
        print("False")
    except AttributeError:
        print("True")

    try:
        inst.val  # ошибка
        print("False")
    except AttributeError:
        print("True")

    try:
        inst.line()  # ошибка
        print("False")
    except AttributeError:
        print("True")

    try:
        inst.yyy  # ошибка
        print("False")
    except AttributeError:
        print("True")

    try:
        CustomClass.x  # ошибка
        print("False")
    except AttributeError:
        print("True")
