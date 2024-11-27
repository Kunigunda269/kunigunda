def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    if obj_type == 'int' or obj_type == 'str' or obj_type == 'float':
        methods = [method for method in methods if not method.startswith('__')]
    module = getattr(obj, '__module__', '__main__')

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

obj = ExampleClass(42)
info = introspection_info(obj)
print(info)
number_info = introspection_info(42)
print(number_info)
