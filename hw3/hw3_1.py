class Car:
    def __init__(self, speed:int, color:str, name:str):
        self.__speed = speed
        self.__color = color
        self.__name = name

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed:int):
        self.__speed = new_speed

    def get_name(self):
        return self.__name

    def set_name(self, new_name:str):
        self.__name = new_name

    def get_color(self):
        return self.__color

    def set_color(self, new_color:str):
        self.__color = new_color

car = Car(120, 'black', 'android')

print(car.get_speed())
car.set_speed(150)
print(car.get_speed())

print(car.get_name())
car.set_name('coolcar')
print(car.get_name())

print(car.get_color())
car.set_color('blue')
print(car.get_color())