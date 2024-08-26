# str1 = 'a a a b c a a d c d d'
# str1 = str1.split()
# my_dict = {}
# for i in str1:
#     if i not in my_dict:
#         my_dict[i] = 0
#         print(i, end=" ")
#     else:
#         my_dict[i] += 1
#         print(f'{i}_{my_dict[i]}', end=' ')
# #Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# # слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.
# #Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# # I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
#
# print(len(set(input().lower().split())))
n = int(input())
max_number = -1
while n > 0: #1
   n = int(input())
   if max_number < n:
       n = max_number
print(n)