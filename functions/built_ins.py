# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'oktbr': ['bishkek_oktbr', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.0.12'],
#     '1may': ['bishkek_1may', 'Jibek-Jolu 212', 'Belyi Dom', 'Cisco', '11.255.10.12'],
#     'svrdl': ['bishkek_svrdl', 'Ahunbaeva 212', 'TC', 'Cisco', '11.25.105.12']
# }
# bishkek_data = {}

# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data)

# ------------------------------
# all(), any()

# all(Iterable) - Возращает True, если все элементы итерируемого объекта истина, иначе False


# ls = [[1,2], 5, 'stroka', True, 1, '']
# print(all(ls)) # -> True

# ip = '10.255.0.155' # True
# ip1 = '10.124.0y.202' # False

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)

# any - Возвращает True, если хотябы один элемент истинна

# ls = [0, 0, [], 0]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite commandu: ') # rmdir test
#         # False, False, False, False
# if any(x in command for x in ignore):
#     raise Exception('Block you!')
# print('OK!')


# -----------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat


# symbols = '_()+-@!#%'
# q_pass = int(input('Vvedite kol-vo paroley: '))


# result = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }

# print(result)
# print(f'Quantity of passwords: {len(result)}')

# from statistics import mean

# avg = mean(len(x) for x in result)
# print(f'Avg len of passwords: {avg}')

