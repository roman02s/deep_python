import weakref


class PlansCommon:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class PlansSlots:
    __slots__ = ("a", "b", "c")

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class PlansEnd:
    def __init__(self, p: "PlansRef"):
        self.p = weakref.ref(p)


class PlansRef:
    def __init__(self):
        self.p_1 = PlansEnd(self)
