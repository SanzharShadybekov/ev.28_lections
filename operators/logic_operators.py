# Операторы сравнения
# Условные операторы и логические операторы

# операторы сравнения
# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 5 -> True
# 7 > 9 -> False

# Условные операторы
# if 
# elif
# else

# if <condition>:
#     <body if> # сработает если в condition if придет true
# [elif] <condition>:
#     <body elif> 
# [else]:
#     <body else> # сработает если во всех выше стоящих условиях пришло False

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello, it\'s me\nI was wondering if after all these years you\'d like to meet')
# elif string.lower() == 'john':
#     print('Welcome back John Snow! The King of North!')
# elif string.lower() == 'abra-kadabra':
#     print('Sim Salamon Kadabra')
# else:
#     print('Совпадений не найдено!')

# print('Registration Form:')
# email = input('Enter your email: ')
# password = input('Enter the password: ')
# if len(password) < 8: # 6
#     raise ValueError('Password is too short!\nNeed to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Password is invalid!\nPassword must contain symbols too!')
# elif password.isalpha():
#     raise ValueError('Password is invalid!\nPassword must contain number or special symbols too!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#     raise ValueError('Passwords did not match!')

# print(f'Successfully registered! Hello Mr/Mrs {email}!')

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18: 
#     print(f'Access Denied! Come again after {18 - age} year!')
# else:
#     print('You can pass! Welcome to KZ!')

# and - логическое и
# or - лог или
# not - лог отрицание

# money = 1_000_001
# status = 'premium'

# if money > 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re ministr of our club!')
# else:
#     print('You\'re honorable member of our club!')

# str1 = 'hello world'
# print(str1)
# symbol = input('Enter the symbol: ')

# if symbol not in str1:
#     print(f'The symbol: {symbol} does not exists!')
# else:
#     print(f'The symbol: {symbol} exists') 

# if symbol in str1:
#     print(f'The symbol: {symbol} exists')
# else:
#     print(f'The symbol: {symbol} does not exists!')

# разрешаем доступ если он юзер гита или гугла и его возраст больше 21 или у него деньги(10000)
# user = 'John'
# is_google_user = True
# is_github_user = False
# age = 21
# user_coins = 110

# if (is_github_user or is_google_user) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')

