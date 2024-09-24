def test_function():
    def inner_function(name):
        print(f"я {name} области видимости функции test_function")

    inner_function("volva")
    inner_function("kunigunda")

test_function()

print("внутренняя функция не доступна")
