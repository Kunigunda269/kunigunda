class Animal:
    alive = True  
    fed = False   

    def __init__(self, name):
        self.name = name 

    def eat(self, food):
        if food.edible:  
            print(f"{self.name} съел {food.name}")
            self.__class__.fed = True  
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.__class__.alive = False  


class Plant:
    edible = False  
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass  


class Predator(Animal):
    pass  


class Flower(Plant):
    pass  


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.__class__.edible = True  


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
