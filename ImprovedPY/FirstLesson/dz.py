# import os
#
#
# def rename_files(desired_name, num_digits, source_ext, target_ext):
#     os.chdir("test_folder")
#     count = 1
#     for file in os.listdir("."):
#         if file.split('.')[-1] == source_ext:
#             os.rename(file, f"{desired_name}{str(count).rjust(num_digits, '0')}.{target_ext}")
#             count += 1
#
#     os.chdir("..")
#
#
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
#
#
# import os
# import json
# import csv
# import pickle
#
#
# def traverse_directory(directory):
#     data = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             data.append({"Path": os.path.join(root, file),
#                          "Type": "File",
#                          "Size": os.path.getsize(os.path.join(root, file))})
#         for cur_dir in dirs:
#             data.append({"Path": os.path.join(root, cur_dir),
#                          "Type": "Directory",
#                          "Size": get_dir_size(os.path.join(root, cur_dir))})
#     return data
#
#
# def get_dir_size(directory):
#     summa = 0
#     for file in os.listdir(directory):
#         if os.path.isdir(os.path.join(directory, file)):
#             summa += get_dir_size(os.path.join(directory, file))
#         else:
#             summa += os.path.getsize(os.path.join(directory, file))
#     return summa
#
#
# # def get_dir_size(directory):
# #     total_size = 0
# #
# #     for root, dirs, files in os.walk(directory):
# #         for name in files:
# #             path = os.path.join(root, name)
# #             total_size += os.path.getsize(path)
# #
# #     return total_size
#
#
# def save_results_to_json(results, name):
#     with open(name, 'w', encoding="utf-8") as file:
#         json.dump(results, file)
#
#
# def save_results_to_csv(results, name):
#     with open(name, "w", encoding="utf-8", newline="") as f:
#         w = csv.DictWriter(f, results[0].keys())
#         w.writeheader()
#         w.writerows(results)
#
#
# def save_results_to_pickle(results, name):
#     with open(name, 'wb') as handle:
#         pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# results = traverse_directory("test_folder")
# save_results_to_json(results, 'results.json')
# save_results_to_csv(results, 'results.csv')
# save_results_to_pickle(results, "results.pkl")
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan
#
#     def wing_length(self):
#         return self.wingspan / 2
#
#
# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         super().__init__(name)
#         self.max_depth = max_depth
#
#     def depth(self):
#         if self.max_depth < 10:
#             return "Мелководная рыба"
#         elif self.max_depth > 100:
#             return "Глубоководная рыба"
#         else:
#             return "Средневодная рыба"
#
#
# class Mammal(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         self.weight = weight
#
#     def category(self):
#         if self.weight < 1:
#             return "Малявка"
#         elif self.weight > 200:
#             return "Гигант"
#         else:
#             return "Обычный"
#
#
# class AnimalFactory:
#     def create_animal(*args):
#         if args[0] == "Bird":
#             return Bird(args[1], args[2])
#         elif args[0] == "Fish":
#             return Fish(args[1], args[2])
#         elif args[0] == "Mammal":
#             return Mammal(args[1], args[2])
#         else:
#             raise ValueError("Недопустимый тип животного")
#
#
# # animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# # animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('srgerh', 'Слон', 5000)
#
# # print(animal1.wing_length())
# # print(animal2.depth())
# print(animal3.category())
#
# class LotteryGame:
#     def __init__(self, lst1, lst2):
#         self.lst1 = lst1
#         self.lst2 = lst2
#
#
#     def compare_lists(self):
#         counter = 0
#         new_list = []
#         for i in range(len(self.lst1)):
#             if self.lst1[i] in self.lst2:
#                 counter += 1
#                 new_list.append(self.lst1[i])
#         if counter > 0:
#             print(f"Совпадающие числа: {new_list}")
#             print(f"Количество совпадающих чисел: {counter}")
#         else:
#             print("Совпадающих чисел нет")
#
#
# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
# game = LotteryGame(list1, list2)
# matching_numbers = game.compare_lists()
#
# from random import randint
# import csv
# import json
# from math import sqrt
#
#
# def generate_csv_file(file_name: str, rows: int) -> None:
#     with open(file_name, mode="w", encoding='utf-8') as w_file:
#         file_writer = csv.writer(w_file, lineterminator="\r")
#         for i in range(rows):
#             file_writer.writerow([randint(1, 100), randint(1, 100), randint(1, 100)])
#
#
# def save_to_json(func):
#     def inner(*args, **kwargs):
#         with open(args[0], newline='') as csv_read_file:
#             data_list = csv.reader(csv_read_file)
#             new_data = []
#             for row in data_list:
#                 result = func(row)
#                 new_data.append({"parameters": row, "result": result})
#             with open("results.json", 'w') as json_write_file:
#                 json.dump(new_data, json_write_file)
#
#     return inner
#
#
# @save_to_json
# def find_roots(*args, **kwargs):
#     a, b, c = map(int, *args)
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         return None
#     elif d == 0:
#         return [-b / (2 * a)]
#     else:
#         return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
#
#
# generate_csv_file("input_data.csv", 1500)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==1500)
#
#
# from datetime import datetime
# class MyStr(str):
#     def __new__(cls, value, author):
#         instance = super().__new__(cls, value)
#         instance.value = value
#         instance.author = author
#         instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
#         return instance
#
#     def __str__(self):
#         return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"
#
#     def __repr__(self):
#         return f"{MyStr.__name__}('{self.value}', '{self.author}')"
#
#
# event = MyStr("Завершилось тестирование", "John")
# print(event)
# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))
#
# class Archive:
#     _instance = None
#
#     def __new__(cls, text, number):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.archive_text = []
#             cls._instance.archive_number = []
#         cls._instance.archive_text.append(text)
#         cls._instance.archive_number.append(number)
#         return cls._instance
#
#     def __init__(self, text, number):
#         self.text = text
#         self.number = number
#
#     def __str__(self):
#         return f"Text is {self.text} and number is {self.number}. /
#         Also {self._instance.archive_text} and {self._instance.archive_number}"
#
#     def __repr__(self):
#         return f"{Archive.__name__}({self.text}, {self.number})"
#
# class Rectangle:
#     def __init__(self, width, height=None):
#         self.width = min(width, height) if height is not None else width
#         self.height = height if height is not None else width
#
#     def perimeter(self):
#         return 2 * self.width + 2 * self.height
#
#     def area(self):
#         return self.width * self.height
#
#     def __add__(self, other):
#         return Rectangle(self.width + other.width, self.height + other.height)
#
#     def __sub__(self, other):
#         return Rectangle(self.width - other.width, self.height - other.height)
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __le__(self, other):
#         return self.area() <= other.area()
#
#     def __str__(self):
#         return f'Прямоугольник со сторонами {self.width} и {self.height}'
#
#     def __repr__(self):
#         return f"{Rectangle.__name__}(width={self.width}, height={self.height})"
#
#
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")
# class Matrix:
#     def __init__(self, rows: int, cols: int):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for j in range(cols)] for i in range(rows)]
#
#     def __str__(self):
#         matr = ""
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if i == self.rows - 1 and j == self.cols - 1:
#                     matr += f"{self.data[i][j]}"
#                 else:
#                     if j == self.cols - 1:
#                         matr += f"{self.data[i][j]}\n"
#                     else:
#                         matr += f"{self.data[i][j]} "
#         return matr
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.rows}, {self.cols})"
#
#     def __eq__(self, other):
#         flag = True
#         if self.rows == other.rows and self.cols == other.cols:
#             for i in range(self.rows):
#                 for j in range(self.cols):
#                     if self.data[i][j] != other.data[i][j]:
#                         flag = False
#         else:
#             flag = False
#         return flag
#
#     def __add__(self, other):
#         new_matrix = None
#         if self.rows == other.rows and self.cols == other.cols:
#             new_matrix = Matrix(self.rows, self.cols)
#             for i in range(self.rows):
#                 for j in range(self.cols):
#                     new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
#         return new_matrix
#
#     def __mul__(self, other):
#         new_matrix = None
#         if self.cols == other.rows:
#             new_matrix = Matrix(self.rows, other.cols)
#             for i in range(self.rows):
#                 for j in range(other.cols):
#                     for k in range(self.cols):
#                         new_matrix.data[i][j] += self.data[i][k] * other.data[k][j]
#         return new_matrix
#
#
# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]
#
# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]
#
# result = matrix3 * matrix4
# print(result)
# import csv
#
#
# class Student:
#     def __init__(self, name: str, subjects: str):
#         self.name = None
#         self.validator_name(name)
#         self.__subjects = dict()
#         self.__load_subjects(subjects)
#
#     # def __setattr__(self, name, value):
#     #     if name == name.upper() and name.isalpha():
#     #         self.name = value
#
#     # def __getattr__(self, name):
#     #     pass
#
#     def validator_name(self, name):
#         if name == name.title() and name.replace(' ', '').isalpha():
#             self.name = name
#         else:
#             raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
#
#     def __str__(self):
#         lst_subjects = list(self.__get_student_subjects())
#         f_str = f"Студент: {self.name}\nПредметы: "
#         for elem in lst_subjects:
#
#             if elem != lst_subjects[-1]:
#                 f_str += elem + ", "
#             else:
#                 f_str += elem
#         return f_str
#
#     def __get_student_subjects(self):
#         lst_subjects = []
#         for subj, grades in self.__subjects.items():
#             for name, mark in grades.items():
#                 if mark and subj not in lst_subjects:
#                     lst_subjects.append(subj)
#         return lst_subjects
#
#     def __load_subjects(self, subjects_file):
#         with open(subjects_file, 'r', newline='', encoding="utf-8") as f:
#             reader = csv.reader(f)
#             data = [row for row in reader]
#             dict_data = dict()
#             for elem in data[0]:
#                 dict_data[elem] = {"Grade": [], "Test_score": []}
#             # self.__subjects.update(dict_data)
#             self.__subjects = dict_data
#
#     def add_grade(self, subject, grade):
#         if subject not in self.__subjects:
#             return f"Предмет {subject} не найден"
#         else:
#             if 2 <= grade <= 5:
#                 self.__subjects[subject]["Grade"].append(grade)
#             else:
#                 raise ValueError("Оценка должна быть целым числом от 2 до 5")
#
#     def add_test_score(self, subject, test_score):
#         if subject not in self.__subjects:
#             return f"Предмет {subject} не найден"
#         else:
#             if 0 <= test_score <= 100:
#                 self.__subjects[subject]["Test_score"].append(test_score)
#             else:
#                 raise ValueError("Результат теста должен быть целым числом от 0 до 100")
#
#     def get_average_test_score(self, subject):
#         if subject not in self.__subjects:
#             raise ValueError(f"Предмет {subject} не найден")
#         return sum(item for item in self.__subjects[subject]["Test_score"]) / len(
#             self.__subjects[subject]["Test_score"])
#
#     def get_average_grade(self, ):
#         grades = []
#         for item in self.__subjects:
#             for grade in self.__subjects[item]["Grade"]:
#                 grades.append(grade)
#         return sum(grades) / len(grades)
#
#
# student = Student("Иван Иванов", "subjects.csv")
#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
#
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
#
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
#
# print(student)

# Введите ваше решение ниже

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
#     def perimeter(self):
#         """
#         Вычисляет периметр прямоугольника.
#
#         Возвращает:
#         - int: периметр прямоугольника
#         """
#         return 2 * (self.width + self.height)
#
#     @property
#     def width(self):
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
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value < 0:
#             raise NegativeValueError("Высота", value)
#         self._height = value
#
#     def area(self):
#         """
#         Вычисляет площадь прямоугольника.
#
#         Возвращает:
#         - int: площадь прямоугольника
#         """
#         return self.width * self.height
#
#     def __add__(self, other):
#         """
#         Определяет операцию сложения двух прямоугольников.
#
#         Аргументы:
#         - other (Rectangle): второй прямоугольник
#
#         Возвращает:
#         - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
#         """
#         width = self.width + other.width
#         perimeter = self.perimeter() + other.perimeter()
#         height = perimeter // 2 - width
#         return Rectangle(width, height)
#
#     def __sub__(self, other):
#         """
#         Определяет операцию вычитания одного прямоугольника из другого.
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
#         height = perimeter // 2 - width
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
#
#
# r = Rectangle(3, 4)
# r.width = -3
#
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# from typing import Union
#
#
# class Archive:
#     """
#     Класс, представляющий архив текстовых и числовых записей.
#
#     Атрибуты:
#     - archive_text (list): список архивированных текстовых записей.
#     - archive_number (list): список архивированных числовых записей.
#     - text (str): текущая текстовая запись для добавления в архив.
#     - number (int или float): текущая числовая запись для добавления в архив.
#     """
#
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.archive_text = []
#             cls._instance.archive_number = []
#         else:
#             cls._instance.archive_text.append(cls._instance.text)
#             cls._instance.archive_number.append(cls._instance.number)
#         return cls._instance
#
#     def __init__(self, text: str, number: Union[int, float]):
#         if not isinstance(text, str) or text == '':
#             raise InvalidTextError(text)
#         else:
#             self.text = text
#         if (not isinstance(number, int) and not isinstance(number, float)) or number < 0:
#             print(isinstance(number, int), isinstance(number, float))
#             raise InvalidNumberError(number)
#         else:
#             self.number = number
#
#     def __str__(self):
#         return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'
#
#     def __repr__(self):
#         return f'Archive("{self.text}", {self.number})'
#
#
# # Введите ваше решение ниже
# class InvalidTextError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"Invalid text: {self.value}. Text should be a non-empty string."
#
#
# class InvalidNumberError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"Invalid number: {self.value}. Number should be a positive integer or float."
#
#
# # a1 = Archive(565, 1)
# # print(a1)
# invalid_archive_instance = Archive("", -5)
# print(invalid_archive_instance)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class InvalidNameError(Exception):
#     pass
#
#
# class InvalidAgeError(Exception):
#     pass
#
#
# class InvalidIdError(Exception):
#     pass
#
#
# class Person:
#     def __init__(self, name, surname, patronymic, age):
#         if name == '':
#             raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
#         self.name = name
#         if surname == '':
#             raise InvalidNameError(f'Invalid name: {surname}. Name should be a non-empty string.')
#         self.surname = surname
#         if patronymic == '':
#             raise InvalidNameError(f'Invalid name: {patronymic}. Name should be a non-empty string.')
#         self.patronymic = patronymic
#         if not isinstance(age, int) or age < 1:
#             raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
#         self.age = age
#
#     def birthday(self):
#         self.age += 1
#
#     def get_age(self):
#         return self.age
#
#
# class Employee(Person):
#     def __init__(self, name, surname, patronymic, age, employee_id):
#         super().__init__(name, surname, patronymic, age)
#         if not isinstance(employee_id, int) or employee_id < 100000 or employee_id > 999999:
#             raise InvalidIdError(f'Invalid id: {employee_id}. Id should be a 6-digit positive integer between '
#                                  f'100000 and 999999.')
#         self.id = employee_id
#
#     def get_level(self):
#         return self.id % 7
#
#
# e1 = Employee('qweqwe', 'b', 'c', 12, 100000)
# print(f'{e1.name} {e1.surname} {e1.patronymic} {e1.age} {e1.id}')
# print(e1.get_age())
# print(e1.get_level())
# Введите ваше решение ниже
# Введите ваше решение ниже
class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        >>> Employee("Ivanov","Ivan","Ivanovich",30, "manager", 50000).full_name()
        'Ivanov Ivan Ivanovich'
        >>> Employee("ivanov","ivan","ivanovich",30, "manager", 50000).last_name
        'Ivanov'
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        >>> e1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> e1.birthday()
        >>> e1.get_age()
        31

        """
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


# Введите ваше решение ниже

def test_employee_raise_salary():
    """
     >>> emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
     >>> emp.raise_salary(10)
     >>> emp.salary
     55000.0

     """

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # e1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    # print(e1.full_name())
