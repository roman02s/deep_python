def base_mapping(name: str):
    return f"custom_{name}"


def is_danger_method(name: str):
    if name.startswith("__") and name.endswith("__"):
        return True
    return False


class CustomMeta(type):
    _mapping = base_mapping

    def __new__(cls, future_class_name,
                future_class_parents, future_class_attrs):
        magic_attrs: dict = {}
        attrs: dict = {}
        for name, value in future_class_attrs.items():
            if is_danger_method(name):
                magic_attrs[name] = value
            else:
                attrs[cls._mapping(name)] = value
        new_class = super().__new__(
            cls, future_class_name,
            future_class_parents, dict(**attrs, **magic_attrs)
        )

        def prefix_mapping(attr_name, attr_value):
            if is_danger_method(attr_name):
                return attr_name, attr_value
            return cls._mapping(attr_name), attr_value

        def meta_setattr(obj, attr_name, value):
            attr_name, value = prefix_mapping(attr_name, value)
            obj.__dict__[attr_name] = value

        new_class.__setattr__ = meta_setattr
        return new_class

    @staticmethod
    def mapping(mapping=base_mapping):
        CustomMeta._mapping = mapping
        return CustomMeta
