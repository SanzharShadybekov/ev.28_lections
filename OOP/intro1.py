# ООП - объектно-ориентированное программирование 

# Класс -> это описание того, как должен выглядеть объект, то есть в классемы описываем какими свойствами(данными) и поведением(фукнции) должен обладать объект

# Объект -> эьл сущность которую мы создаем от класса, у объекта есть собственное состояние свойств(данные)

# целью создания было связать данные с фукнциями которые управляли этими данными

# Свойствами(аттрибутами) - называют обычные переменные внутри класса, в которых хранятся данные объекта

# Методы - это обычные функции внутри класса, методы описывают поведение объекта

# ---------------------------

# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'


# john = Human('John', 'Snow', 'King of North', 'Northerner')
# billal = Human('Billal', 'Lanister', 'Programmist', 'KR')

# # print(john, type(john))
# # print(dir(john))
# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'King of Westeros'
# print(john.show_info())
# print()
# print(billal.show_info())


# -----------------
# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         "Инициализатор,  именно здесь создаются аттрибуты объекта"
#         # self - ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')
    
#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')

# rex = Dog('Rex', 'black')
# pluto = Dog(name='Pluto', color='brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()

# --------------------------
# class Human:
#     def __init__(self):
#         print('init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100
    
#     def eat(self, meal, doela=True):
#         print(f"{self.raychel} покушала {meal}")
#         if doela:
#             if self.golod < 50:
#                 self.golod = 0
#             else: 
#                 self.golod -= 50
#         else:
#             self.golod -= 25

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)