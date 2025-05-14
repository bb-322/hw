class Rectangle:
    def __init__(self, lenght:int, width:int, color:str):
        self.length = lenght
        self.width = width
        self.color = color
    def __str__(self):
        return f'length: {self.length}\nwidth: {self.width}\ncolor: {self.color}'

class Button():
    def __init__(self, size:int, color:str):
        self.size = size
        self.button_color = color

    def click(self):
        return f'{self.button_color} button with the size of {self.size} m^3 is clicked with a 2D rectangle'

star = Rectangle(2, 3, 'black')
print(star)
click = Button(10, 'red').click()
print(click)