import pytest


#
#
# class NegativeValueError(ValueError):
#     pass
#
#
# class Rectangle:
#     def __init__(self, width, height=None):
#         if width <= 0:
#             raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
#         self._width = width
#         if height is None:
#             self._height = width
#         else:
#             if height <= 0:
#                 raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
#             self._height = height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self._width = value
#         else:
#             raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value > 0:
#             self._height = value
#         else:
#             raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
#
#     def perimeter(self):
#         return 2 * (self._width + self._height)
#
#     def area(self):
#         return self._width * self._height
#
#     def __add__(self, other):
#         width = self._width + other._width
#         perimeter = self.perimeter() + other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height)
#
#     def __sub__(self, other):
#         if self.perimeter() < other.perimeter():
#             self, other = other, self
#         width = abs(self._width - other._width)
#         perimeter = self.perimeter() - other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height)
#
#
# # Введите ваше решение ниже
#
# def test_width():
#     rect = Rectangle(5)
#     assert rect.width == 5
#
#
# def test_height():
#     rect = Rectangle(3, 4)
#     assert rect.height == 4
#
#
# def test_perimeter():
#     rect = Rectangle(5)
#     assert rect.perimeter() == 20
#
#
# def test_area():
#     rect = Rectangle(3, 4)
#     assert rect.area() == 12
#
#
# def test_addition():
#     rect = Rectangle(5, 3)
#     rect2 = Rectangle(1, 4)
#     rect3 = rect + rect2
#     assert rect3.width == 8
#     assert rect3.height == 5
#
#
# def test_negative_width():
#     with pytest.raises(NegativeValueError):
#         Rectangle(-5)
#
#
# def test_negative_height():
#     with pytest.raises(NegativeValueError):
#         Rectangle(5, -4)
#
#
# def test_set_width():
#     rect = Rectangle(5)
#     rect.width = 10
#     assert rect.width == 10
#
#
# def test_set_negative_width():
#     rect = Rectangle(5)
#     with pytest.raises(NegativeValueError):
#         rect.width = -10
#
#
# def test_set_height():
#     rect = Rectangle(3, 4)
#     rect.height = 6
#     assert rect.height == 6
#
#
# def test_set_negative_height():
#     rect = Rectangle(3, 4)
#     with pytest.raises(NegativeValueError):
#         rect.height = -6
#
#
# def test_subtraction():
#     rect = Rectangle(10, 4)
#     rect2 = Rectangle(3, 1)
#     rect3 = rect - rect2
#     assert rect3.width == 7
#     assert rect3.height == 3
#
# def test_subtraction_negative_result():
#     rect = Rectangle(10, 4)
#     rect2 = Rectangle(3, 1)
#     with pytest.raises(NegativeValueError):
#         rect3 = rect - rect2
#
#
# def test_subtraction_same_perimeter():
#     rect = Rectangle(5, 1)
#     rect2 = Rectangle(4, 3)
#     rect3 = rect - rect2
#     assert rect3.width == 1
#     assert rect3.height == -2
class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def test_employee_full_name():
    assert Employee("Ivanov", "Ivan", "Ivanovich", 30,
                                  "manager", 50000).full_name() == "Ivanov Ivan Ivanovich"


def test_employee_birthday():
    emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    emp.birthday()
    assert emp.get_age() == 31


def test_employee_raise_salary():
    emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    emp.raise_salary(10)
    assert emp.salary == 55000.0

def test_employee_str():
    emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    assert str(emp) == "Ivanov Ivan Ivanovich (Manager)"

def test_employee_last_name_title():
    emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    assert emp.last_name == "Ivanov"