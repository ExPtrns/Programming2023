# import doctest
#
#
# class NegativeValueError(Exception):
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#
#     def __str__(self):
#         return f'{self.name} должна быть положительной, а не {self.value}'
#
#
# class Rectangle:
#     """
#     Класс, представляющий прямоугольник.
#
#     Атрибуты:
#     - width (int): ширина прямоугольника
#     - height (int): высота прямоугольника
#
#     Методы:
#     - perimeter(): вычисляет периметр прямоугольника
#     - area(): вычисляет площадь прямоугольника
#     - __add__(other): определяет операцию сложения двух прямоугольников
#     - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
#     - __lt__(other): определяет операцию "меньше" для двух прямоугольников
#     - __eq__(other): определяет операцию "равно" для двух прямоугольников
#     - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
#     - __str__(): возвращает строковое представление прямоугольника
#     - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
#     """
#
#     def __init__(self, width, height=None):
#         if width < 0:
#             raise NegativeValueError("Ширина", width)
#         else:
#             self.width = width
#         if height is None:
#             self.height = width
#         else:
#             if height < 0:
#                 raise NegativeValueError("Высота", height)
#             else:
#                 self.height = height
#
#     @property
#     def width(self):
#         """
#         >>> r1 = Rectangle(5)
#         >>> r1.width
#         5
#         >>> r4 = Rectangle(-2)
#         Traceback (most recent call last):
#           ...
#         NegativeValueError: Ширина должна быть положительной, а не -2
#         """
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value < 0:
#             raise NegativeValueError("Ширина", value)
#         self._width = value
#
#     @property
#     def height(self):
#         """
#         >>> r2 = Rectangle(3, 4)
#         >>> r2.width
#         3
#         >>> r2.height
#         4
#         """
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value < 0:
#             raise NegativeValueError("Высота", value)
#         self._height = value
#
#     def perimeter(self):
#         """
#         Вычисляет периметр прямоугольника.
#         >>> r1 = Rectangle(5)
#         >>> r1.perimeter()
#         20
#
#         Возвращает:
#         - int: периметр прямоугольника
#         """
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         """
#         Вычисляет площадь прямоугольника.
#         >>> r1 = Rectangle(5)
#         >>> r1.area()
#         25
#
#         Возвращает:
#         - int: площадь прямоугольника
#         """
#         return self.width * self.height
#
#     def __add__(self, other):
#         """
#         Определяет операцию сложения двух прямоугольников.
#         >>> r1 = Rectangle(5)
#         >>> r2 = Rectangle(3, 4)
#         >>> r3 = r1 + r2
#         >>> r3.width
#         8
#         >>> r3.height
#         6.0
#
#         Аргументы:
#         - other (Rectangle): второй прямоугольник
#
#         Возвращает:
#         - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
#         """
#         width = self.width + other.width
#         perimeter = self.perimeter() + other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height)
#
#     def __sub__(self, other):
#         """
#         Определяет операцию вычитания одного прямоугольника из другого.
#         >>> r1 = Rectangle(5)
#         >>> r2 = Rectangle(3, 4)
#         >>> r3 = r1 - r2
#         >>> r3.width
#         2
#         >>> r3.height
#         2.0
#
#
#         Аргументы:
#         - other (Rectangle): вычитаемый прямоугольник
#
#         Возвращает:
#         - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
#         """
#         if self.perimeter() < other.perimeter():
#             self, other = other, self
#         width = abs(self.width - other.width)
#         perimeter = self.perimeter() - other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height)
#
#     def __lt__(self, other):
#         """
#         Определяет операцию "меньше" для двух прямоугольников.
#
#         Аргументы:
#         - other (Rectangle): второй прямоугольник
#
#         Возвращает:
#         - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
#         """
#         return self.area() < other.area()
#
#     def __eq__(self, other):
#         """
#         Определяет операцию "равно" для двух прямоугольников.
#
#         Аргументы:
#         - other (Rectangle): второй прямоугольник
#
#         Возвращает:
#         - bool: True, если площади равны, иначе False
#         """
#         return self.area() == other.area()
#
#     def __le__(self, other):
#         """
#         Определяет операцию "меньше или равно" для двух прямоугольников.
#
#         Аргументы:
#         - other (Rectangle): второй прямоугольник
#
#         Возвращает:
#         - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
#         """
#         return self.area() <= other.area()
#
#     def __str__(self):
#         """
#         Возвращает строковое представление прямоугольника.
#
#         Возвращает:
#         - str: строковое представление прямоугольника
#         """
#         return f"Прямоугольник со сторонами {self.width} и {self.height}"
#
#     def __repr__(self):
#         """
#         Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
#
#         Возвращает:
#         - str: строковое представление прямоугольника
#         """
#         return f"Rectangle({self.width}, {self.height})"