
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

result1 = apply_all_func([6, 20, 15, 9], max, min)
result2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

