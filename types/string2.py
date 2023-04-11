
# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# # print(a != b)
# # print('abc' == 'abc')
# print(a > b)
# print(a < b)

# print('a') # 97 -> 1100001
# print('a' > 'b') # 97 > 98
# print('h' > 'c') # 104 > 99
# print('hello' > 'harry') # True
# print('abc' > 'abc') # False

# len() - возвращает кол-во символов в строке 
# a = 'Hello'
# b = 'john snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# >, <, ==, !=, >=, <=

# Методы строк
# replace(old, new, [count]) - меняет в строке символы old на new, если вы укажете count, то заменит count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'e')
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))


# isdigit   -           Проверяют
# isnumeric - ->  состоит ли наша строка 
# isdecimal -      полностью из чисел

# num = input('Vvedite chislo: ')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинкского алфавита и киррилицы
# str1 = '56aаннр你好'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью их символов алфавита

# text = 'Hello world'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Ms. My Name'
# print(str1.islower())
# print(str1.istitle())
# str2 = 'RTY UIOp'
# print(str2.isupper())

# index(value, [start], [end]) - выводит индекс значения value, которое мы передаем, в нашей строке.

# text = 'Hello john snow'
# print(text.index('John', 2, 5))

# text = 'Hello world! My name is John Snow!' # o
# # print(text.index('John'))
# res = text.index('o')
# print(res) # 4
# res = text.index('o', res + 1)
# print(res) # 7
# res = text.index('o', res + 1)
# print(res) # 25
# res = text.index('o', res + 1)
# print(res) # 31

# count(value, [start]) - считает кол-во вхождений value в нашу строку 

# text = 'hello o o o hello'
# print(text.count('o'))
# print(text.count('hello'))
# print(text.count('ghj'))

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части сохраняются в типе list

# text = 'Let me speak by my hearth in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# print(len(res))


# a = '#hello#hello#hello#hello'
# res = a[1:].split('#')
# print(res)

# 'connector'.join(list) -> cоединяет по connector строки которые находились в list

# text = 'Let me speak by my hearth in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# str1 = ' '.join(res)
# print(str1)


# find(value, [start], [end]) - делает тоже самое что и index, но если не нашел то вернется -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('lytui'), type(text.find('lytui')))
# print('John Snow')

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

          # john.capitalize() -> John
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'jOHN edart snow'
# print(fio.title())
# print(fio.capitalize())

# print(dir(str))
