from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass


class Blue(Color):
    def fill_color(self):
        print("Filling in blue color")


class Red(Color):
    def fill_color(self):
        print("Filling in red color")


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, color: Color):
        super().__init__(color)

    def draw(self):
        print("Draw rectangle")
        self.color.fill_color()


class Circle(Shape):
    def __init__(self, color: Color):
        super().__init__(color)

    def draw(self):
        print("Draw circle")
        self.color.fill_color()


def client_code(shape: Shape):
    shape.draw()


if __name__ == '__main__':
    circle_color = Blue()
    rectangle_color = Red()

    circle_shape = Circle(circle_color)
    rectangle_shape = Rectangle(rectangle_color)

    for shape_element in [circle_shape, rectangle_shape]:
        client_code(shape_element)
