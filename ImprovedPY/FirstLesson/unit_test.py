import unittest

from dz import Employee


#
#
# class NegativeValueError(ValueError):
#     pass
#
#
# class Rectangle:
#
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
# class TestRectangle(unittest.TestCase):
#     def test_width(self):
#         self.assertEqual(Rectangle(5).width, 5)
#
#     def test_height(self):
#         self.assertEqual(Rectangle(3, 4).height, 4)
#
#     def test_perimeter(self):
#         self.assertEqual(Rectangle(5).perimeter(), 20)
#
#     def test_area(self):
#         self.assertEqual(Rectangle(3, 4).area(), 12)
#
#     def test_addition(self):
#         self.assertEqual(Rectangle(5).__add__(Rectangle(3, 4)).width, 8)
#         self.assertEqual(Rectangle(5).__add__(Rectangle(3, 4)).height, 6)
#
# if __name__ == '__main__':
#     unittest.main()


class TestEmployee(unittest.TestCase):
    def test_employee_full_name(self):
        self.assertEqual(Employee("Ivanov", "Ivan", "Ivanovich", 30,
                                  "manager", 50000).full_name(), "Ivanov Ivan Ivanovich")

    def test_employee_birthday(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30,
                       "manager", 50000)
        emp.birthday()
        self.assertEqual(emp.get_age(), 31)

    def test_employee_raise_salary(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30,
                       "manager", 50000)
        emp.raise_salary(10)
        self.assertEqual(emp.salary, 55000.0)

    def test_employee_str(self):
        self.assertEqual(Employee("Ivanov", "Ivan", "Ivanovich", 30,
                                  "manager", 50000).__str__(), "Ivanov Ivan Ivanovich (Manager)")

    def test_employee_last_name_title(self):
        self.assertIsNot(Employee("Ivanov", "Ivan", "Ivanovich", 30,
                                  "manager", 50000).last_name, "Ivan")
