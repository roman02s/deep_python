def base_mapping(name: str):
    return f"custom_{name}"


class CustomMeta(type):
    _mapping = base_mapping

    def __new__(mcs, future_class_name, future_class_parents, future_class_attrs):
        print(f"{future_class_name=}, {future_class_parents=}, {future_class_attrs=}")
        attrs: dict = dict((name, value) for name, value in future_class_attrs.items() if "__" in name)
        upper_attrs: dict = dict((mcs._mapping(name), value) for name, value in future_class_attrs.items() if not name.startswith("__") and not name.endswith("__"))

        new_class = super().__new__(mcs, future_class_name, future_class_parents, dict(**attrs, **upper_attrs))

        def prefix_mapping(attr_name, attr_value):
            if attr_name.startswith("__") and attr_name.endswith("__"):
                return attr_name, attr_value
            return mcs._mapping(attr_name), attr_value

        def meta_setattr(obj, attr_name, value):
            attr_name, value = prefix_mapping(attr_name, value)
            obj.__dict__[attr_name] = value

        new_class.__setattr__ = meta_setattr

        return new_class

    @staticmethod
    def mapping(cls, mapping=base_mapping):
        cls._mapping = mapping
        print("set mapping")
        return cls
