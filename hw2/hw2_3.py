class Vehicle:
    def __init__(self):
        pass

class Car(Vehicle):
    def __init__(self, color:str, max_speed:int):
        super(Vehicle).__init__()
        self.on_land = True
        self.color = color
        self.max_speed = max_speed
    
    def __str__(self):
        return f'{self.on_land}, {self.color}, {self.max_speed}'
        

class Boat(Vehicle):
    def __init__(self, color:str, max_speed:int):
        super(Vehicle).__init__()
        self.on_water = True
        self.color = color
        self.max_speed = max_speed
    def __str__(self):
        return f'{self.on_water}, {self.color}, {self.max_speed}'


class Amphibian(Car, Boat):
    def __init__(self, color: str, max_speed: int):
        super().__init__(color, max_speed)
        self.on_water = True      # added manually since in line 26 --> class Amphibian(Car, Boat): <-- "Car" goes first, thus only adding "self.on_land = True"
    
    def __str__(self):
        return f'{self.on_land}, {self.on_water}, {self.color}, {self.max_speed}'

car = Car
boat = Boat
amphibian = Amphibian

print(car('red', 100))
print(boat('blue', 40))
print(amphibian('white', 100))
print('Amphibian MRO: ', [cls.__name__ for cls in Amphibian.__mro__])