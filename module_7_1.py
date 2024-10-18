class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.file_name = 'products.txt'

    def get_products(self):
        file = open(self.file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        file = open(self.file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str not in existing_products:
                file.write(product_str + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()


shop = Shop()
potato = Product('Potato', 50.5, 'Vegetables')
spaghetti = Product('Spaghetti', 3.4, 'Groceries')
another_potato = Product('Potato', 5.5, 'Vegetables')

print(spaghetti)

shop.add(potato, spaghetti, another_potato)

print(shop.get_products())
