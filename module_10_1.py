import threading
from time import sleep, perf_counter

# Функция для записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунда
    print(f"Завершилась запись в файл {file_name}")

# Запуск функций без потоков
start_time = perf_counter()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = perf_counter()
print(f"Время выполнения функций: {end_time - start_time}")

# Запуск функций в потоках
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt')),
]

start_time = perf_counter()
for thread in threads:
    thread.start()  # Запуск потока

for thread in threads:
    thread.join()  # Ожидание завершения потока

end_time = perf_counter()
print(f"Время выполнения потоков: {end_time - start_time}")
