my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_1 = 0
while list_1 < len(my_list):
    if my_list[list_1] < 0:
        break
    if my_list[list_1] != 0:  # Игнорируем нулевые значения
        print(my_list[list_1])
    list_1 += 1
print('список закончен')
