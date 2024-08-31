# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# list_1 = 0
# while list_1 < len(my_list):
#     if my_list[list_1] < 0:
#         break
#     print(my_list[list_1])
#     list_1+=1
# print('список закончен')

# a = int(input('введите числитель:'))
# b = int(input('введите знаменатель:'))

# while True:
#     result = a % b
#     print (result)
#     result == input('yes/no')
#     if result >= 0:
#         break
#     elif unput_1 == input('yes'):
#         a = int(input('введите числитель:'))
#         b = int(input('введите знаменатель:'))
#     else:
#         print('error')


a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))

while True:
    remainder = a % b
    print(f'Остаток от деления: {remainder}')

    user_input = input('Введите "yes" для продолжения или "no" для выхода: ')

    if user_input.lower() == 'no':
        break
    elif user_input.lower() == 'yes':
        a = int(input('Введите новый числитель: '))
        b = int(input('Введите новый знаменатель: '))
    else:
        print('Некорректный ввод. Попробуйте снова.')
