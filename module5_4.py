class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, floors):
        self.numberOfFloors = floors
        self.name = name


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



house1 = House('ЖК Гарант', 12)
print(House.houses_history)
house2 = House('ЖК Панорама', 21)
print(House.houses_history)
print(House.houses_history[0])
print(house2.name)
house2.__del__()
print(House.houses_history)
