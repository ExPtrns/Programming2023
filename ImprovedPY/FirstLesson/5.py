"""Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""
from Tools.demo import queens

# def my_gen(count):
#     result = 2
#     if count == 1:
#         yield result
#     else:
#         for i in range(count):
#            result= i+1
#     yield result
#
# print(*my_gen(5))


# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

# Введите ваше решение ниже
# print({names[i]: salary[i]*(int(bonus[i][:-1]))/100 for i in range(len(names))})
# def fibonacci():
#     a, b = 0, 1
#     for _ in range(10000000):
#         yield a
#         a, b = b, a + b
#
#
#
#
# f = fibonacci()
# for i in range(10):
#     print(next(f))

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# def get_next_prime(num):
#     if num == 1:
#         return 2
#     counter = num + 1
#     while True:
#         for i in range(num, counter):
#             if len([i for i in range(1, counter + 1) if counter % i == 0]) < 3:
#                 return counter
#             else:
#                 counter += 1
#
#
# # вызываем функцию
# print(get_next_prime(13))


# объявление функции
# def is_password_good(password):
#     flag = [len(password) > 7,
#             password.lower() != password,
#             password.upper() != password,
#             any(map(str.isdigit, password))]
#     return all(flag)
#
#
# # вызываем функцию
# print(is_password_good("aabbcc11op"))
# def date_to_prove(date_check):
#     day, month, year = map(int, date_check.split("."))
#     if year <= 0:  # проверка года
#         return False
#     if month < 1 or month > 12:  # проверка месяца
#         return False
#     print(day, month, type(month), len(str(year)))
#
#
# def year_check(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         return True

# print(date_to_prove('15.3.2023'))
# объявление функции
# def is_one_away(word1, word2):
#     if len(word1) == len(word1):
#         check = [False for i in range(len(word1)) for j in word2[i] if word1[i] != word2[i]]
#         if len(check)==1:
#             return True
#     return False
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))

# def is_palindrome(text):
#     new_text = "".join((symbol.lower() for symbol in text if symbol not in ",.!?- "))
#     return new_text == new_text[::-1]
#
#
# print(is_palindrome("Standart - smallest, sell Amstrad nats"))


# объявление функции
# def is_valid_password(password):
#     if len(password.split(":")) != 3:
#         return False
#     first, second, third = password.split(":")
#     check = [first == first[::-1],
#              is_prime(int(second)),
#              int(third) % 2 == 0
#              ]
#     return all(check)
#
# def is_prime(num):
#     if num == 1:
#         return False
#     if len([i for i in range(1, num + 1) if num % i == 0]) > 2:
#         return False
#     else:
#         return True
#
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))

#
# def is_correct_bracket(text):
#     if len(text) % 2 != 0:
#         return False
#     counter = 1
#     for b in text:
#         if counter < 1:
#             return False
#         if b == "(":
#             counter += 1
#         elif b == ")":
#             counter -= 1
#     return True if counter == 1 else False
#
# # считываем данные
# print(is_correct_bracket("(((("))

# def convert_to_python_case(text):
#     camel = ""
#     for i in range(0, len(text) - 1):
#         camel += text[i].lower()
#         if text[i + 1] == text[i + 1].upper() and not text[i + 1].isdigit():
#             camel += "_"
#     camel += text[len(text)-1]
#     return camel
# # считываем данные
# print(convert_to_python_case('ThisIsCamelCased'))


# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
#
# print(get_middle_point(0, 0, 10, 0))
# print(get_middle_point(1, 5, 8, 3))

# from math import pi
#
# # объявление функции
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius ** 2
#     return c, s
#
# # считываем данные
# print(get_circle(1))
# print(get_circle(1.5))

# from math import sqrt
# # объявление функции
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d == 0:
#         x1 = x2 = -b / (2 * a)
#     else:
#         x1, x2 = (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)
#     if x1 < x2:
#         return x1, x2
#     else:
#         return x2, x1
#
# # считываем данные
# # вызываем функцию
# print(solve(1, -4, -5))
# print(solve(-2, 7, -5))
# print(solve(1, 2, 1))
# print(solve(22, 34, -8))

# def draw_triangle():
#
#     for i in range(1, 9):
#         print(" " * (8 - i), end="")
#         print("*" * (2*i-1))


# основная программа
# draw_triangle()  # вызов функции


# # объявление функции
# def get_shipping_cost(quantity):
#     cost = 1000
#     for i in range(1,quantity):
#         cost += 120
#     return cost
#
# # считываем данные
# print(get_shipping_cost(1))
# print(get_shipping_cost(3))


# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     list_10 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
#                'восемнадцать', 'девятнадцать']
#     list_20 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num < 10:
#         return list_1[num - 1]
#     elif 9 < num < 20:
#         return list_10[num - 10]
#     else:
#         nums, tens = num % 10, num // 10
#         if nums == 0:
#             return list_20[tens-2]
#         else:
#             return f"{list_20[tens-2]} {list_1[nums - 1]}"
#
# print(number_to_words(99))
# объявление функции
# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#               'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#               'november', 'december']
#     if language == "ru":
#         return lng_ru[number-1]
#     else:
#         return lng_en[number - 1]
#
# print(get_month('ru', 1))
# print(get_month('ru', 12))
# print(get_month('en', 1))
# print(get_month('en', 10))


# объявление функции
# def is_magic(date):
#     day, month, year = map(int, (date.split(".")))
#     year = year % 100
#     return day * month == year
#
#
# print(is_magic('10.06.1960'))
# print(is_magic('11.06.1960'))
#
# def is_pangram(text):
#     my_set = set("".join(text.split()).lower())
#     lst = sorted(list(my_set))
#     return True if lst[0] == "a" and lst[len(lst) - 1] == "z" and len(lst) == 26 else False
#
#
# print(is_pangram('Jackdaws love my big sphinx of quartz'))
# print(is_pangram('The jay pig fox zebra and my wolves quack'))
# print(is_pangram('Hello world'))

# from math import factorial
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n-k)))
#
#
# # вызываем функцию
# print(compute_binom(10, 2))


# import math
# print(math.ceil(math.log(int(input()), 2)))

# encryption_or_decryption = input('Шифрование или дешифрование?')
# language = input('Русский или английский?')
# # k = int(input('Шаг сдвига (со сдвигом вправо)?'))
# alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
# s = input('Введите строку')
# s1 = ''
# for k in range(24):
#     if encryption_or_decryption.lower() == 'шифрование':
#         if language.lower() == 'русский':
#             for c in s:
#                 if c in alphabet_RU:
#                     s1 += alphabet_RU[(alphabet_RU.find(c) + k) % 32]
#                 elif c in alphabet_ru:
#                     s1 += alphabet_ru[(alphabet_ru.find(c) + k) % 32]
#                 else:
#                     s1 += c
#         elif language.lower() == 'английский':
#             for c in s:
#                 if c in alphabet_EN:
#                     s1 += alphabet_EN[(alphabet_EN.find(c) + k) % 26]
#                 elif c in alphabet_en:
#                     s1 += alphabet_en[(alphabet_en.find(c) + k) % 26]
#                 else:
#                     s1 += c
#     if encryption_or_decryption.lower() == 'дешифрование':
#         if language.lower() == 'русский':
#             for c in s:
#                 if c in alphabet_RU:
#                     s1 += alphabet_RU[(alphabet_RU.find(c) - k) % 32]
#                 elif c in alphabet_ru:
#                     s1 += alphabet_ru[(alphabet_ru.find(c) - k) % 32]
#                 else:
#                     s1 += c
#         elif language.lower() == 'английский':
#             for c in s:
#                 if c in alphabet_EN:
#                     s1 += alphabet_EN[(alphabet_EN.find(c) - k) % 26]
#                 elif c in alphabet_en:
#                     s1 += alphabet_en[(alphabet_en.find(c) - k) % 26]
#                 else:
#                     s1 += c
#     print(s1)

# SYMBOLS_IN_ALPHABET = 26
# LAST_BIG_CHR = 90
# LAST_SMALL_CHR = 122
#
#
# def get_crypto_koef(word):
#     k = 0
#     for char in word:
#         if char.isalpha():
#             k += 1
#     return k
#
#
# def get_ord(char, k) -> int:
#     if ord(char) in range(ord("A"), ord("Z")):
#         if ord(char) + k > LAST_BIG_CHR:
#             return ord(char) - SYMBOLS_IN_ALPHABET + k
#         else:
#             return ord(char) + k
#     else:
#         if ord(char) + k > LAST_SMALL_CHR:
#             return ord(char) - SYMBOLS_IN_ALPHABET + k
#         else:
#             return ord(char) + k
#
#
# def encrypt_text(string):
#     words = string.split()
#     encrypted = ""
#     for word in words:
#         for char in word:
#             if char.isalpha():
#                 encrypted += chr(get_ord(char, get_crypto_koef(word)))
#             else:
#                 encrypted += char
#         encrypted += " "
#     return encrypted.rstrip()
#
#
# print(encrypt_text(input()))

import random

# def is_attacking(q1, q2):
#     if q1[0] == q2[0] or q1[1] == q2[1]:
#         return True
#     # + +
#     for i in range(1, 8):
#         if q1[0] + i > 8 or q1[1] + i > 8:
#             break
#         else:
#             if q1[0] + i == q2[0] and q1[1] + i == q2[1]:
#                 return True
#     # + -
#     for i in range(1, 8):
#         if q1[0] + i > 8 or q1[1] - i < 1:
#             break
#         else:
#             if q1[0] + i == q2[0] and q1[1] - i == q2[1]:
#                 return True
#     # - +
#     for i in range(1, 8):
#         if q1[0] - i < 1 or q1[1] + i > 8:
#             break
#         else:
#             if q1[0] - i == q2[0] and q1[1] + i == q2[1]:
#                 return True
#     # - -
#     for i in range(1, 8):
#         if q1[0] - i < 1 or q1[1] - i < 1:
#             break
#         else:
#             if q1[0] - i == q2[0] and q1[1] - i == q2[1]:
#                 return True
#     return False
#
#
# def check_queens(queens):
#     for i in range(len(queens) - 1):
#         for j in range(i + 1, len(queens)):
#             if is_attacking(queens[i], queens[j]):
#                 return False
#     return True
#
# def generate_boards():
#     board_list = []
#     queens = [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]
#     if check_queens(queens):
#         board_list.append(queens)
#     queens = [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)]
#     if check_queens(queens):
#         board_list.append(queens)
#     queens= [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)]
#     if check_queens(queens):
#         board_list.append(queens)
#     queens = [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]
#     if check_queens(queens):
#         board_list.append(queens)
#     return board_list
#     # for i in range(8):
#     #     queens.append((random.randint(1, 8), random.randint(1, 8)))
#     # board_list = []
#     # while len(board_list) < 4:
#     #     if check_queens(queens):
#     #         board_list.append(queens)
#     #         print(board_list)
#
#
# print(generate_boards())

# for i in range(2012):
#     lst = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
#     print(lst[i % 12])

people = list(range(1, 7 + 1))
step = 5
t = step - 1
while len(people) > 1:
    del people[t]
    t -= 1
    if t + step < len(people):
        t += step
    else:
        for _ in range(step):
            t += 1
            if t > len(people) - 1:
                t = 0
print(people)
