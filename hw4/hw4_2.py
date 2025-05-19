class Calculator:
    def __init__(self, num1: int, num2:int):
        self.num1 = num1
        self.num2 = num2
    
    def summ(self):
        return (self.num1 + self.num2)
    
    def sub(self):
        return (self.num1 - self.num2)
    
    def mult(self):
        return (self.num1 * self.num2)
    
    def div(self):
        try:
            return (self.num1 / self.num2)
        except ZeroDivisionError:
            return "can't divide by zero"
    
    def pwr(self):
        try:
            return (self.num1 ** self.num2)
        except ZeroDivisionError:
            return "can't divide by zero"

action = Calculator

print(action(8, 2).div())
print(action(10, 0).div())
print(action(2, 3).pwr())
print(action(0, -1).pwr())