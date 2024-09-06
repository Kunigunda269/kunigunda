def generate_password(n):
    result = []
    used_pairs = set()
    for i in range(1, n):
        for j in range(i + 1, n):
            pair_sum = i + j
            if pair_sum % n == 0:
                pair = (i, j)
                if pair not in used_pairs:
                    used_pairs.add(pair)
                    result.append(f'{i}{j}')
    return ''.join(result)


n = int(input("введите число от 3 до 20: "))
password = generate_password(n)
print(f"сгенерированный пароль для числа {n}: {password}")
