class House:
    def __init__(self, floors, name):
        self.numberOfFloors = floors
        self.name = name


    def __len__(self):
        return self.numberOfFloors


    def __str__(self):
        return f'Название: {self.name}; кол-во этажей: {self.numberOfFloors}'


    def __eq__(self, other):
       return self.numberOfFloors == other.numberOfFloors

    def __lt__(self, other):
        return self.numberOfFloors < other.numberOfFloors


    def __le__(self, other):
        return self.numberOfFloors <= other.numberOfFloors


    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors


    def __ge__(self, other):
        return self.numberOfFloors >= other.numberOfFloors


    def __ne__(self, other):
        return self.numberOfFloors != other.numberOfFloors


    def __add__(self, value):
        return self.numberOfFloors + value


    def __radd__(self, value):
        return value + self.numberOfFloors

    def __iadd__(self, value):
        return self.numberOfFloors += value



house1 = House(12, 'ЖК Гарант')
house2 = House(21, 'ЖК Панорама')
print(len(house1))
print(len(house2))
print(house1)
print(house2)
house1.numberOfFloors=21
print(house1)
print(house1 == house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 >= house2)
print(house1 != house2)
house1 = house1 + 3
print(house1)
house1 = 3 + house1
print(house1)
house1 += 10
print(house1)
