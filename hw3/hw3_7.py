# example_7.py
from PIL import Image, ImageDraw


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new("RGBA", (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new("RGBA", (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save("picture.png", quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill="yellow", outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save("draw-circle.png", quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill="blue", outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save("draw-square.png", quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save("draw-triangle.png", quality=95)


class Cone(Shape):
    def draw(self):
        
        cone_top = (400, 100)
        cone_base_left = (350, 200)
        cone_base_right = (450, 200)
        ellipse_box = (350, 190, 450, 210)

        gradient_layer = Image.new("RGB", self.im.size)
        draw_grad = ImageDraw.Draw(gradient_layer)

        for x in range(350, 451):
            brightness = int(100 + 155 * (x - 350) / 100)
            draw_grad.line([(x, 100), (x, 200)], fill=(brightness, brightness, brightness))

        mask = Image.new("L", self.im.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.polygon([cone_top, cone_base_left, cone_base_right], fill=255)

        self.im.paste(gradient_layer, (0, 0), mask)

#-------------------------------------------------------------------------

        base_layer = Image.new("RGB", self.im.size)
        draw_base = ImageDraw.Draw(base_layer)

        for x in range(350, 451):
            brightness = int(100 + 155 * (x - 350) / 100)
            draw_base.line([(x, 190), (x, 210)], fill=(brightness, brightness, brightness))

        base_mask = Image.new("L", self.im.size, 0)
        base_mask_draw = ImageDraw.Draw(base_mask)
        base_mask_draw.pieslice(ellipse_box, start=0, end=180, fill=255)

        self.im.paste(base_layer, (0, 0), base_mask)

        draw = ImageDraw.Draw(self.im)
        draw.arc(ellipse_box, start=0, end=180, fill=(60, 60, 60), width=2)

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)
        self.draw1.ellipse([(350, 150), (450, 250)], fill=self.back_color)

    def save(self):
        print("Image with cone was created")
        return self.im.save("draw-cone.png", quality=95)

    
class Paraboloid(Shape):
    def draw(self):
        ellipse_bot = (100, -100, 400, 500)
        self.draw1.pieslice(ellipse_bot, 0, 180, fill=(255, 255, 255))

        gradient_layer = Image.new("RGB", self.im.size)
        draw_grad = ImageDraw.Draw(gradient_layer)

        for x in range(-100, 501):
            brightness = 255 - int(100 + 155 * (x - 300) / 100)
            draw_grad.line([(x, -100), (x, 500)], fill=(brightness, brightness, brightness))
        
        mask_bot = Image.new("L", self.im.size, 0)
        mask_bot_draw = ImageDraw.Draw(mask_bot)
        mask_bot_draw.pieslice(ellipse_bot, 0, 180, fill=255)

        self.im.paste(gradient_layer, (0, 0), mask_bot)
#----------------------------------------------------------------------------------------------        
        ellipse_top = (100, 150, 400, 250)
        self.draw1.ellipse(ellipse_top, fill=(255, 255, 255))

        gradient_layer = Image.new("RGB", self.im.size)
        draw_grad = ImageDraw.Draw(gradient_layer)

        for y in range(150, 250):
            brightness = 255 - (int(100 + 155 * (y - 200) / 100))
            draw_grad.line([(100, y), (400, y)], fill=(brightness, brightness, brightness))
        
        mask_top = Image.new("L", self.im.size, 0)
        mask_top_draw = ImageDraw.Draw(mask_top)
        mask_top_draw.ellipse(ellipse_top, fill=255)

        self.im.paste(gradient_layer, (0, 0), mask_top)
        
        # self.draw1.arc(ellipse_top, start=0, end=360, fill=(60, 60, 60), width=4)
    
    def erase(self):
        self.draw1.pieslice((100, -100, 400, 500), 0, 180, fill=self.back_color)
        self.draw1.ellipse((100, 150, 400, 250), fill=self.back_color)

    def save(self):
        print("Image with paraboloid was created")
        return self.im.save("draw-paraboloid.png", quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(
            input(
                "\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник"
                "\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t"
                "8. Вихід з програми\n9. Конус\n10. Зафарбувати конус\n11. Параболоїд\n12. Зафарбувати параболоїд\nОберіть необхідний пункт меню: "
            )
        )
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                break
            case 9:
                co = Cone()
                work_with_obj(co)
            case 10:
                co = Cone()
                update_obj(co)
            case 11:
                par = Paraboloid()
                work_with_obj(par)
            case 12:
                par = Paraboloid()
                update_obj(par)
            case _:
                print("Оберіть пункт меню корректно!!!")


if __name__ == "__main__":
    menu()
