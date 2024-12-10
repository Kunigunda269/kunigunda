import logging
from runner_module import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class RunnerTest:
    @staticmethod
    def test_walk():
        try:
            # Создаем объект с неправильной скоростью
            r1 = Runner("Вася", -5)
            r1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.warning(e)

    @staticmethod
    def test_run():
        try:
            # Создаем объект с неправильным именем
            r2 = Runner(2)
            r2.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(e)
            
if __name__ == "__main__":
    RunnerTest.test_walk()
    RunnerTest.test_run()
    print("Тесты выполнены. Проверьте файл runner_tests.log для логов.")
