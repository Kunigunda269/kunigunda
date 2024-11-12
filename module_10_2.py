import threading
import time

ENEMIES = 100
lock = threading.Lock()


class Knight:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.days = 0

    def fight(self):
        global ENEMIES
        print(f"{self.name}, на нас напали!")

        while True:
            with lock:
                if ENEMIES <= 0:
                    break
                ENEMIES = max(0, ENEMIES - self.power)

            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {ENEMIES} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
first_thread = threading.Thread(target=first_knight.fight)
second_thread = threading.Thread(target=second_knight.fight)
first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()
print("Все битвы закончились!")
