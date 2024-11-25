#данная библиотека может работаь очень много делать разного с эксель файлами и многими другими.
# Большиий упор делается на работе с цифрами, код ниже дает возможность прочитать первые 5 строк файла.
# Вторая часть кода группирует данные по значению в указанных столбцах файла

import pandas as pd
data = pd.read_excel('C:\\Users\\User\\OneDrive\\Рабочий стол\\Bybit-UM_2.xlsx')
print("Первые 5 строк:")
print(data.head())

if 'Wallet Balance' in data.columns and 'Funding' in data.columns:
    grouped_data = data.groupby('Wallet Balance')['Funding'].mean()
    print("\nСреднее значение по категориям:")
    print(grouped_data)
else:
    print("\nОшибка: В файле отсутствуют необходимые столбцы 'Category' и 'Value'. Проверьте структуру файла.")


#Следующая библиотека нампай тоже очень полезна.
# Позволяет совершать различные математические операции, в том числе и поиск среднего
import numpy as np
array = np.array([1, 2, 3, 4, 5])

# Операции: сложение, умножение и нахождение среднего значения
array_sum = np.sum(array)
array_product = np.prod(array)
array_mean = np.mean(array)

print("Сумма элементов:", array_sum)
print("Произведение элементов:", array_product)
print("Среднее значение элементов:", array_mean)

#Библиотека имеет функцию построения графиков разной сложности с последующим сохраанением в различных форматах
import matplotlib.pyplot as plt

# Данные для построения графика
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# Построение столбчатого графика
plt.bar(categories, values, color='skyblue')
plt.title('Пример столбчатого графика')
plt.xlabel('Категории')
plt.ylabel('Значения')
# Сохранение графика
plt.savefig('bar_chart.png')
plt.show()



