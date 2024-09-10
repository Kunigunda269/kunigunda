def generate_password(n):
    result = []

    for i in range(1, n):
        for j in range(i + 1, n):
            result.append(f'{i}{j}')

    result.sort()

    return ''.join(result)

test_values = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
for n in test_values:
    password = generate_password(n)
    print(f"сгенерированный пароль для числа {n}: {password}")
