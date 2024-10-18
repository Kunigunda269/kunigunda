class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Метод, который возвращает строку в формате '<название>, <вес>, <категория>'
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                # Читаем все продукты из файла
                products = file.read()
            return products
        except FileNotFoundError:
            # Если файл еще не создан, вернем пустую строку
            return ""

    def add(self, *products):
        existing_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for product in products:
                # Проверяем, есть ли продукт в магазине
                if product.__str__() not in existing_products:
                    file.write(product.__str__() + '\n')
                else:
                    print(f'Продукт {product} уже есть в магазине')


# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Проверим метод __str__ для продукта p2
print(p2)

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем список продуктов из файла
print(s1.get_products())
