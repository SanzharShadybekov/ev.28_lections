# 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# 'you! meet to Nice Snow. is name'

# 'hello world snow king'
# 'king snow world hello'

# str1 = 'Hello world! My name is John, last name is Snow. Nice to meet you!'

# def get_reversed_string(text):
#     # print(text[::-1])
#     spisok = text.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)

# print(get_reversed_string(str1))
# print(get_reversed_string('hello world snow king'))

# def sum_of_args(a, b, c=5, d=5): # параметры
#     return a + b + c + d

# result = sum_of_args(1, 2, 3, 4) # аргументы
# print(result)
# res = sum_of_args
# # print(res, type(res))
# print(res(5, 6, 7, 8))
# print(sum_of_args(5, 5))

# ---------------------------------
# позиционные и именованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(5, 10, 15)
# print()
# printParams(c=5, b=15, a=10)
# print()
# a = 100
# printParams(a=20, b=a, c=15)


# def sum_of_args(a, b, c, d): 
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments(позиционные аргументы)
# print(sum_of_args(a=5, c=20, b=10, d=15)) # keyword arguments(именованные аргументы)
# print(sum_of_args(5, 10, d=15, c=20))

# -------------------
# оператор *
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

# -----------------------
# *args, **kwargs в фукнциях

# def printScores(student, *scores):
#     print(f'Name of student: {student}')
#     # print(*scores)
#     print(f'AVG: {sum(scores) / len(scores)}')
#     for x in scores:
#         print('Score:', x)

# printScores('John Snow', 100, 90, 80, 95, 88)


# def printPetNames(owner, **pets): #{'key': 'value'}
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori', 'Batya'], turtle='Leonardo')

# def get_some_data(a, b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print('аргументы:', args)
#     print('именованные аргументы:', kwargs)

# get_some_data(1,2,3,4,5, lang='Python', car='BMW')

# ---------------------
def generate_random_string(len_):
    import string as s
    import random
    # print(s.ascii_letters, s.digits, s.punctuation)
    symbols = s.ascii_letters + s.digits
    res = list(
        random.choice(symbols) for i in range(1, len_)
    ) + list(random.choice(s.punctuation))
    random.shuffle(res)
    return ''.join(res)

print(generate_random_string(15))
print(generate_random_string(20))
print(generate_random_string(8))
print(generate_random_string(8))








