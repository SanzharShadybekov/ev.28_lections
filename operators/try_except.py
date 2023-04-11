# Обработка исключений
# операторы try..except

# Errors -> связаны с кодом
    # SyntaxError
    # IndentationError
    # TabError

# Исключения exceptions -> связаны с неправильными данными которые передаются в код
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError 
    # KeyError
    # BaseException # прородитель всех исключений

# try:
# a = int(input('Enter the number: '))
# except:
#     print('неправильные данные!')
# else:
#     print(a * 5)

# try:
    # <body>
# except:
    # <body> сработает если есть ошибка
# <else>:
    # <body> если нет ошибки
# <finally>:
    # <body> сработает в люом случае

# ls = ['John', 'Snow', 'Tririon']
# print(ls)
# try:
#     i = int(input('Vvedite Index: '))
#     print(ls[i])
# except ValueError:
#     print('Вы ввели неправильные данные')
# except IndexError:
#     print('Вы ввели неправильный индекс')

# --------------------
# отображение ошибки
# Exception as e (error)
# dict_ = {'1': 'one', '2': 'two', 'name': 'John'}

# try:
#     key = input('Vvedite key: ')
#     print(dict_[key])
# except Exception as e:
#     print(f'Opps {e.__class__} error!')

# try:
#     num1 = int(input('Enter num1: '))
#     num2 = int(input('Enter num2: '))
#     result = num1 / num2
# except ValueError:
#     print('Invalid input!')
# except ZeroDivisionError:
#     print('Na 0 delit\' nel\'zya!')
# else:
#     print(result)
# finally:
#     print('The End!')




