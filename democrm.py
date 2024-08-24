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
