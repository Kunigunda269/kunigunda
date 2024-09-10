def generate_password(n):
    result = []

    for i in range(1, n):
        for j in range(i + 1, n):
            pair_sum = i + j
            if n % pair_sum == 0:
                result.append(f'{i}{j}')

    return ''.join(result)


test_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for n in test_values:
    password = generate_password(n)
    print(f"сгенерированный пароль для числа {n}: {password}")
