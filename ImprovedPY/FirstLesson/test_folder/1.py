# # user_input = input('Enter data: ')
# #
# # if user_input.isdigit():
# #     user_input = int(user_input)
# # elif user_input.replace('-', '').replace('.', '').isdigit() and \
# #         user_input.count('.') < 2 and '-' not in user_input[1:]:
# #     user_input = float(user_input)
# # elif user_input.lower() != user_input:
# #     user_input = user_input.lower()
# # else:
# #     user_input = user_input.upper()
# #
# # print(user_input)
# # print(type(user_input))
# #
# # data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
# #
# # my_dict = {}
# # my_list = []
# # for item in data:
# #     my_dict[item] = data.count(item)
# #
# # for item in my_dict:
# #     if my_dict.get(item) != 2:
# #         my_list.append(item)
# # print(my_list)
#
#
# # items = {
# #     "ключи": 0.3,
# #     "кошелек": 0.2,
# #     "телефон": 0.5,
# #     "зажигалка": 0.1
# #
# # }
# # max_weight = 1.0
# #
# # # Введите ваше решение ниже
# # backpack = {}
# # all_weight = 0
# # for item, weight in items.items():
# #     if all_weight + weight <= max_weight:
# #         backpack[item] = weight
# #         all_weight += weight
# # print(backpack)
# """
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами. Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
# """
# import hashlib
# # text = "Python 3.9 is the latest version of Python. It's awesome! aaa aaa aaa bbb bbb bbb bbb"
# #
# # # Введите ваше решение ниже
# # BAD_SYMBOLS = "\\*_{}[]()>#+-,.!$123456789"
# #
# # result = []
# # my_dict = {}
# # text = text.replace("'", " ")
# # for char in BAD_SYMBOLS:
# #     if char in text:
# #         text = text.replace(char, "")
# # text = text.lower().split()
# # for word in text:
# #     my_dict[word] = my_dict.get(word, 0) + 1
# #
# # for key, counter in my_dict.items():
# #     result.append((key, counter))
# # result.sort(reverse=True)
# # result.sort(key=lambda a: a[1], reverse=True)
# #
# # print(result[:10])
#
# # lst = [1, 1, 2, 2, 3, 3]
#
# # Введите ваше решение ниже
# # my_set = set()
# # for item in lst:
# #     if lst.count(item) > 1:
# #         my_set.add(item)
# # print(list(my_set))
#
# # def transpose(matr):
# #     rows = zip(*matr)
# #     return [list(row) for row in rows]
# #
# #
# #
# #
# #
# # matrix = [[1, 2, 3],
# #          [4, 5, 6],
# #          [7, 8, 9]]
# # transposed_matrix = transpose(matrix)
# #
# # # Введите ваше решение ниже
# # print(transposed_matrix)
# # Введите ваше решение ниже
#
#
# # def key_params(**kwargs) -> {}:
# #     print(kwargs)
# #     for item in kwargs:
# #         print(kwargs.get(item))
# #     # my_list = ["a", a, "b", b, "c", c, "d", d]
# #     # my_dict = {}
# #     # for i in range(0, len(my_list), 2):
# #     #     if my_list[i + 1].__hash__:
# #     #         my_dict[my_list[i + 1]] = my_list[i]
# #     #     else:
# #     #         my_dict[str(my_list[i + 1])] = my_list[i]
# #     # return my_dict
# #
# #
# # params = key_params(name='Alice', age=30, scores=[85, 90, 78], info={'city': 'New York', 'email': 'alice@example.com'})
# # print(params)
#
# import decimal
#
# MULTIPLICITY = 50
# PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# COUNTER4PERCENTAGES = 3
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(1000)
#
# bank_account = decimal.Decimal(0)
# count = 0
# operations = []
#
#
# # Введите ваше решение ниже
# def check_multiplicity(amount):
#     return True if amount % MULTIPLICITY == 0 else False
#
#
# def deposit(amount):
#     global count
#     if check_multiplicity(amount):
#         count += amount
#         operations.append(f'Пополнение карты на {amount} у.е. Итого {count} у.е.')
#     else:
#         print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
#
#
# def withdraw(amount):
#     global count
#     fee = decimal.Decimal(amount) * decimal.Decimal(PERCENT_REMOVAL)
#     if fee < MIN_REMOVAL:
#         fee = MIN_REMOVAL
#     elif fee > MAX_REMOVAL:
#         fee = MAX_REMOVAL
#     if (check_multiplicity(amount)) & (count >= amount + fee) :
#         count -= amount + fee
#         operations.append(f"Снятие с карты {amount} у.е. Процент за снятие {int(fee)} у.е.. Итого {count} у.е.")
#     if not check_multiplicity(amount):
#         print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
#     if count < amount + fee:
#         operations.append(f"Недостаточно средств. Сумма с комиссией {int(amount + fee)} у.е. На карте {count} у.е.")
#
# def exit():
#     global count
#     if count > RICHNESS_SUM:
#         fee_sum = count * RICHNESS_PERCENT
#         count -= fee_sum
#         operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {fee_sum} у.е.'
#                           f' Итого {count} у.е.')
#     operations.append(f'Возьмите карту на которой {count} у.е.')
#
#
# deposit(173)
# withdraw(21)
# exit()
#
# print(operations)
from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True