immutable_var = (15, 215.37, False, 'baltika9')
print (immutable_var)
# immutable_var [1]= 8520
# print(immutable_var)
# элемент кортежа нельзя изменить, поскольку это неизменяемая структура данных
# это сделано для экономии памяти, а также группировки статичных данных разных классов
mutable_list = [23, 315.89, True, 'samorez']
mutable_list[1]= 'kefir'
print(mutable_list)
