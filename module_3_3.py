def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [33.14, 'lincoln', False]
values_dict = {'a': 42, 'b': 'dambldore', 'c': [7, 8, 9]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [123.45, 'cheburek']
print_params(*values_list_2, 42)
