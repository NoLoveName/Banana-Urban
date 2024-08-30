class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat (self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

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
    edible = True


pig = Mammal('поросенок Боря')
apple = Fruit('зеленое яблоко')
panther = Predator ('пантера Альберт')
clover = Flower ('цветущий клевер')

print(pig.name)
print(panther.name)
print(pig.alive)
print(pig.fed)
pig.eat(apple)
print(pig.alive)
print(pig.fed)
print(panther.alive)
print(panther.fed)
panther.eat(clover)
print(panther.alive)
print(panther.fed)
