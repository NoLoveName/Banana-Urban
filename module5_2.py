class House:


    def __init__(self, floors, name):
        self.numberOfFloors = floors
        self.name = name


    def __len__(self):
        return self.numberOfFloors


    def __str__(self):
        return f'Название: {self.name}; кол-во этажей: {self.numberOfFloors}'



house1 = House(12, 'ЖК Гарант')
house2 = House(21, 'ЖК Панорама')
print(len(house1))
print(len(house2))
print(house1)
print(house2)