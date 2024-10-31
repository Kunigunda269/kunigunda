
first_list = ['Strings', 'Student', 'Computers']
second_list = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first) - len(second) for first, second in zip(first_list, second_list) if len(first) != len(second))
second_result = (len(first_list[i]) == len(second_list[i]) for i in range(len(first_list)))

print(list(first_result))
print(list(second_result))
