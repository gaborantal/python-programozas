class Rectangle:
    def __init__(self, length, width, **kwargs):
        print("> Rectangle init STARTED")
        self.length = length
        self.width = width
        super().__init__(**kwargs)  # Comment this
        print("! Rectangle init finished (no base)")

    def area(self):
        print("Rectangle area called")
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        print("> Square init STARTED")
        super().__init__(length=length, width=length, **kwargs)
        print("Square init finished")


class Triangle:
    def __init__(self, base, height, **kwargs):
        print("> Triangle init STARTED")
        self.base = base
        self.height = height
        # super().__init__(**kwargs)
        print("! Triangle init finished (no base)")

    def triangle_area(self):
        return 0.5 * self.base * self.height

    # def area(self):
    #     print("Triangle area called")
    #     return 0.5 * self.base * self.height


class Pyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)
        print("Pyramid init finished")

    def area(self):
        base_area = super().area()
        # triangle_area = Triangle.area(self)
        triangle_area = super().triangle_area()
        return triangle_area * 4 + base_area

    def print_mro(self):
        print(Pyramid.__mro__)


if __name__ == '__main__':
    pyramid = Pyramid(10, 10)
    print(pyramid.area())
    pyramid.print_mro()
