import logging
import argparse

FORMAT = '{levelname}. Catch on : "{asctime}" in file - "{name}" \nDescription - {message}\n'
logging.basicConfig(level=logging.ERROR, filemode='a', encoding='utf-8', filename='log_file.log',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class NegativeValueError(Exception):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        logger.error(f'{self.name} должна быть положительной, а не {self.value}')
        return f'{self.name} должна быть положительной, а не {self.value}'


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width < 0:
            raise NegativeValueError("Ширина", width)
        else:
            self.width = width
        if height is None:
            self.height = width
        else:
            if height < 0:
                raise NegativeValueError("Высота", height)
            else:
                self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError("Ширина", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError("Высота", value)
        self._height = value

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get parameters for Rectangle')
    parser.add_argument('numbers', type=float, nargs='*', help='Enter "width" and "height" for Rectangle')
    args = parser.parse_args()
    params = list(args.numbers)
    params.append(None)
    try:
        r1 = Rectangle(params[0], params[1])
        print(r1)
    except IndexError as ie:
        logger.error("IndexError. Должно быть введено как минимум одно значение.")
        print("Должно быть введено как минимум одно значение.")
    except Exception as ex:
        logger.error(ex)
        raise ex

'''
python Rectangle.py 5
python Rectangle.py -7
python Rectangle.py 4, -7
'''
