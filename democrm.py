import datetime


inventory = {}


def add_item():
   name = input('Введите название товара: ')
   q = int(input('Введите кол-во товара: '))
   price = float(input('Введите цену товара: '))


   if name in inventory:
       inventory[name]['кол-во'] += q
       inventory[name]['цена'] = price
   else:
       inventory[name] = {
           'кол-во':q,
           'цена':price,
           'дата поступления': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       }
   print(f'Товар {name}. Кол-во {q}')


def remove_item():
   name = input('Введите имя товара: ')
   if name in inventory:
       q = int(input('Введите кол-во товара для удаления: '))
       if q <= inventory[name]['кол-во']:
           inventory[name]['кол-во'] -= q
           print(f'Товар {name}. Кол-во {q}')
           if inventory[name]['кол-во'] == 0:
               del inventory[name]
           print(f'Товар {name} полностью удален!')
       else:
           print('Ошибка! товара недостаточно!')
   else:
       print('Ошибка! товара нет на складе!')


def check_inv():
   if inventory:
       print('Текущее состояние склада:')
       for item, details in inventory.items():
           print(f'{item}: кол-во - {details["кол-во"]}, цена - {details["цена"]}, дата - {details["дата поступления"]}.')
   else:
       print('Склад пустой!')


def main_menu():
   while True:
       print("\n--- Система управления складом ---")
       print("1. Добавить товар")
       print("2. Удалить товар")
       print("3. Проверить склад")
       print("4. Выход")


       choice = input('Введите действие(1-3): ')


       if choice == '1':
           add_item()
       elif choice == '2':
           remove_item()
       elif choice == '3':
           check_inv()
       else:
           break


main_menu()


def search_item():
   """Поиск товара на складе"""
   name = input("Введите название товара для поиска: ")
   if name in inventory:
       details = inventory[name]
       print(f"Товар найден: {name}")
       print(f"Количество: {details['quantity']}")
       print(f"Цена за единицу: {details['price']}")
       print(f"Дата добавления: {details['added_date']}")
   else:
       print("Товар не найден на складе")

def calculate_total_value():
   """Расчет общей стоимости товаров на складе"""
   total_value = sum(item['quantity'] * item['price'] for item in inventory.values())
   print(f"Общая стоимость товаров на складе: {total_value:.2f}")

# создание функции
def my_f():
   print("Hello Urban!") # блок действий функции, вывод сообщения на экран


my_f() # вызов функции. Вывод: Hello Urban!
