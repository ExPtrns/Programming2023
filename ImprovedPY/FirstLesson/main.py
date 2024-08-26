# LOWER_LIMIT = 1
# UPPER_LIMIT = 999
# ONE = 1
# TEN = 10
# HUNDRED = 100
#
# number = LOWER_LIMIT - ONE
#
# while number < LOWER_LIMIT or number > UPPER_LIMIT:
#     number = int(input(f'Enter a number in a range from {LOWER_LIMIT} to {UPPER_LIMIT}:\n'))
#
# if number < TEN:
#     result = f'Your number is a digit which square root is: {number * number}'
# elif number < HUNDRED:
#     product = (number // TEN) * (number % TEN)
#     result = f'Your number is a two digit number product is: {product}'
# else:
#     mirror = (number % TEN * HUNDRED) + (number // TEN % TEN * TEN) + (number // HUNDRED)
#     result = f'Your number is a three digit number, mirrored result of which is: {mirror}'
#
# print(f'{result}')
# import fractions

# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f"{j} X {i:<2} = {i*j:<2} ", end="\t")
#     if j > 3:
#         print()
# print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f"{j} X {i:<2} = {i*j:<2} ", end="\t")
#     if j > 3:
#         print()

# num = 0
#
# # Введите ваше решение ниже
# num = hex(num)
# print("Шестнадцатеричное представление числа:", (num.split("0x")[1]).upper())
# print("Проверка результата:", num)


frac1 = "3/7"
frac2 = "1/1"

# Введите ваше решение ниже
frac1 = frac1.split("/")
frac2 = frac2.split("/")
summ = [(int(frac1[0]))*int(frac2[1])+(int(frac1[1]))*int(frac2[0]), int(frac1[1])*int(frac2[1])]
multyp = [(int(frac1[0])) * int(frac2[0]), int(frac1[1]) * int(frac2[1])]
print(fractions.Fraction(summ[0], summ[1]))
print(fractions.Fraction(multyp[0], multyp[1]))
