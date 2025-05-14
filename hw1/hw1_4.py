class Car:
    def __init__(self, name: str, mark: str, color: str, price: str):
        self.mark = mark
        self.color = color
        self.price = price
        self.name = name
    
    def __str__(self):
        return f'{self.name}: \n --- Mark: {self.mark}\n --- Color: {self.color}\n --- Price: {self.price}'

class Carshop:
    def __init__(self, cars: list):
        self.car_list = cars

    def sell_car(self, car_name: Car):
         for car in self.car_list:
            if car.name == car_name:
                self.car_list.remove(car)
                print(f'sold {car_name}')
                return
            else:
                print(f"there's no {car_name}")

    def __str__(self):
        return "\n".join(str(car) for car in self.car_list)

car1 = Car('coolcar', 'Toyota', 'Red', '1$')
car2 = Car('coolercar', 'Tanos', 'Red', '18132457$')
car3 = Car('midcar', 'Valve', 'Red', '320$')
car4 = Car('steam', 'Steam', 'Red', '80500$')
car5 = Car('android', 'iPhone', 'Black', 'free')

cars = [car1, car2, car3, car4, car5]
shop = Carshop(cars)
print(shop)
shop.sell_car('midcar')
print(shop)