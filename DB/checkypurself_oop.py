# 1) Создайте класс MyString, который будет наследоваться от str.
# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'

'''WRITE CODE HERE'''

# 2)Dollar.
# Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
# долларизованный формат:
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
# Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
# init - инициализирует значение атрибута amount
# update - задаёт объекту новое значение amount
# repr - возвращает значение float
# str - метод, который реализует логику функции dollarize()
# //Вывод должен выглядеть следующим образом:
# cash = MoneyFmt(12345678.021)
# print(cash) -- выводит "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- выводит "$100,000.46"
# cash.update(-0.3)
# print(cash) -- выводит "-$0.30"
# repr(cash) -- выводит -0.3

'''WRITE CODE HERE'''

# 3) Велосипед.
# Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
# (стоимость)
# self.make (производитель)
# self.model (модель)
# self.year (год выпуска)
# self.condition (состояние)
# self._sale_price = None (цена для продажи, по умолчанию None)
# self.sold = False (продан или нет, по умолчания False)
# Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
# для указания цены для продажи, который принимает цену и если она меньше стоимости, то
# ставит дефолтную цену для продажи (стоимость + мин. прибыль).
# Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
# ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
# возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
# При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на

# True и возвращает прибыль с продажи.
# Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
# объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
# атрибутов.

'''WRITE CODE HERE'''

# 4) Герой.
# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
# уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
# солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
# "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле
# генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
# героя, принадлежащего команде с более длинным списком, поднимается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
# идентификационные номера этих двух юнитов.

'''WRITE CODE HERE'''