from datetime import date


class MyClass1:

    hoomans = []

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1.hoomans.append(self)

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult(age, country: str):
        if age >= 18 and country == "ua":
            return True
        elif age >= 21 and country == "us":
            return True
        else:
            return False

    @classmethod
    def adult_count(cls, country: str):
        adult_hoomans = []
        for hooman in cls.hoomans:
            if hooman.is_adult(hooman.age, country):
                adult_hoomans.append(hooman)
        return len(adult_hoomans)


hooman1 = MyClass1("surname", "name", 19)
hooman1.print_info()

hooman2 = MyClass1("surname2", "name2", 23)
hooman2.print_info()

hooman3 = MyClass1("surname3", "name3", 16)
hooman3.print_info()


print(hooman1.is_adult(19, "ua"))
print(hooman1.is_adult(19, "us"))
print(hooman2.is_adult(23, "ua"))
print(hooman2.is_adult(23, "us"))
print(hooman3.is_adult(16, "ua"))
print(hooman3.is_adult(16, "us"))

print(MyClass1.adult_count("ua"))
print(MyClass1.adult_count("us"))
