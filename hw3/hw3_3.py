class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        self.temperature = (self.temperature * 1.8) + 32
        return self.temperature

    def to_celsius(self):
        self.temperature = (self.temperature - 32) / (1.8)
        return self.temperature
    
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

temper = Temperature(20)

print(temper.temperature)
print(temper.to_fahrenheit())
print(temper.to_celsius())
temper.temperature = 50
print(temper.temperature)
print(temper.to_fahrenheit())