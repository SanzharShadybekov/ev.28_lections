# while <expression>:
    # <body>

# i = 0
# while i > 10:
#     i += 1 # i = i + 1
#     print(f'Цикл сработал {i} раз!')

# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2: ')
#     print()

#     if i >= 5:
#         print('Цикл остановлен!')
#         break # принудельная остановка
#     i += 1
# else:
#     print('Вы угадали!')


# --------------
# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# # password = None
# while password := input(f'{user["username"]} vvedite parol\': ') != user['password']:
#     # password = input(f'{user["username"]} vvedite parol\': ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!!!')
#         break
# else:
#     print(f'{user["username"]} vy uspeshno zashli v sistemu!')

# ---------------------

# for <variable> in <iterable object>:
    # <body>

# list_ = []
# i = iter(list_)
# print(i)
# print(next(i)) # 1
# print(next(i)) # 2
# print(next(i)) # 3
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# ls = []
# for x in range(1, 101):
#     ls.append(random.randint(1, 50))

# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))

# ls = ['Tirion', 'Bilal', 'John', 'Sansa', 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr/Mrs {x}!')
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    
# число 100
# 1, 2, 4, 5, 10,
# 100, 50, 25, 20, 10

# num = 100_380_450_000_232
# res = []

# for x in range(1, int(num ** 0.5) + 1):
#     if num % x == 0:
#         res.extend({x, num // x})

# res.sort()
# print(res)




