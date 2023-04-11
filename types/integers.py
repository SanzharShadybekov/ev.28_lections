# Типы данных числа -> int, float

# = -> оператор присваивания
# variable(переменная)
# num = 5
# print(num) # 5
# num = 79 # переопределенние
# print(num) # 7

# abc -> нижний регистр
# ABC -> верхний регистр

# PEP8
# tomorrow_day = '10.03.2023' # Snake case
# tomorrowDay = '10.03.2023' # Camel case

# +
# num1 = 5
# num2 = 15
# result = num1 + num2
# print('Summa:', result)

#  -
# num1 = input('Enter the num1: ') # -> '5'
# num2 = input('Enter the num2: ') # -> '7'
# num1 = int(num1)
# num2 = int(num2)
# print(num2, '-', num1, '=', num2 - num1)

# *
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# print(num1, '*', num2, '=', num1 * num2)


# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление(получение остатка от деления)

# num1 = 7
# num2 = 3
# print('/', num1 / num2) # 2.33333...
# print('//', num1 // num2) # 2
# print('%', num1 % num2) # 1

# ** -> возведение в степень
# print(5 ** 2)
# print(16 ** 55)

# print(144 ** 0.5) # квадратный корень

# pow - возведение в степень
# pow(num1, num2, <mod>)
# print(pow(5, 10, 65))
# print(5 ** 10 % 65)

# a = 5
# b = 2
# res = pow(a, b, 3)
# print(res)


# round() - округления числа с плавающей точкой
# a = 5.368232
# print(round(a, 2))

# abs() - абсолютное значение цисла -> abs(-5) -> 5
                                        # |-5| -> 5
# a = abs(-16)
# b = abs(15)
# print(a, b)

# divmod(a, b) -> Она выводит два числа, первое число это результат целочисленного деления(//) a на b, а второе это модульное деление(%) 

# res = divmod(5, 2)
# print(res)
# print((5 // 2, 5 % 2))

# import math

# a = 5
# print(round(math.sqrt(a), 2))
# res = math.sqrt(a)
# print(round(res, 2))


# множественное присваивание
# оператор присваивания(=)
# a = 5
# b = 15
# c = None

# print('a:', a, 'b:', b)

# # c = a
# # a = b
# # b = c
# a, b = b, a 
#       #15, #5
# print('a:', a, 'b:', b)

# num1, num2, num3 = input('num1: '), input('num2: '), input('num3: ')
# print(num1)
# print(num2)
# print(num3)

"""Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал"""
# from math import pi

# r = int(input('Vvedite radius: '))
# res_P = 2 * r * pi 
# res_S = pi * r ** 2
# print('S okruzhnosti: ', round(res_S, 2))
# print('P okruzhnosti: ', round(res_P, 2))

# from random import randint

# # print(randint(1, 10))
# name = input('Vvedite svoe imya: ')
# last_name = input('Vvedite svoyu familiyu: ')
# num = randint(1_000_000, 9_999_999)
# # print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)


from random import randint

# num = randint(1, 10) # 5
# print(num)
# i = 0
# while i < 3: 
#     guess = int(input('Ugadai chislo: ')) # 5
#     if guess == num:
#         print('Ty pobedil! Krasava!')
#         break
#     # i = i + 1 
#     i += 1 # increment

