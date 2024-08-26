'''По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input:       5
Output:    120'''
# name = "Ivan"
# #       0123
# print(name[0])
# foreach - C#
# for element in "Hello", 123, 34.125, True, 'a':
#     print(element * 2)
# 0: element = "Hello"
# 1: element = 123
# 2: element = 34.125
# ...
# range и for между собой НИКАК НЕ СВЯЗАНЫ!!!
# range(begin=необязательный(0), end=обязательный, step=необязательный(+1))
'''
print(*range(5))
# 0 1 2 3 4
print(*range(5, 0, -1))
print(*range(5, 13, 2))
print(*range(2, 10))
print(*range(0, 8, 2))

for i in range(5):
    # print(i, end=' ')
    print(i, end='!\n')

print(1, end=', ')
print(2, end='. ')
print(3, end='!\n')
# print()
print("Hello")

print("Ivan")


from numpy import arange

for i in arange(0.0, 1.23, 0.01):
    print(i)

# Task 9
n = int(input("Input number: "))
result = 1
while n > 1:
    result *= n # result = result * n
    n -= 1
print(result)

Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input:     5
Output:  6
'''
# n = 89
# count = 2
# first = 0
# second = 1
# while second < n:
#     nextNum = first + second
#     first = second
#     second = nextNum
#     count += 1
#     if second > n:
#         count = -1
# print(count)
'''5. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза
Input:	5 -> 5 1 6 5 9
Output:	1 9'''

# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa, min_massa =  x, x
# for i in range(n - 1):
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x:
#         min_massa = x
# print(min_massa, max_massa)
# Task 13
n = int(input("Введите кол-во дней: "))
count = 0
max_count = 0
for i in range(n):
    temp = int(input("Введите температуру: "))
    if temp >= 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print(max_count)