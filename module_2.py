# name = input ('Введите имя: ')
# if name == 'urban':
#     print ('Здравствуйте, администратор')
# else:
#     print('Привет', name)

# name = input('Введите имя: ')
#     if name.isalpha():
#     print('Здравствуйте, администратор')
#     else:
#         print('Привет,', name)
#     else:
#     print('Ошибка: имя должно содержать только буквы.')



number = int(input('введите число: ')) #fizz, buzz, fizzbuzz
if number % 3 == 0 and number % 5 == 0 :
    print('fizzbuzz')
elif number % 3 ==0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print ('Число не подходит')
#or / and