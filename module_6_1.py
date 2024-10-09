
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a_1 = Predator('Волк с Уолл-Стрит')
a_2 = Mammal('Хатико')
p_1 = Flower('Цветик семицветик')
p_2 = Fruit('Заводной апельсин')


print(a_1.name)
print(p_1.name)

print(a_1.alive)
print(a_2.fed)
a_1.eat(p_1)
a_2.eat(p_2)
print(a_1.alive)
print(a_2.fed)
