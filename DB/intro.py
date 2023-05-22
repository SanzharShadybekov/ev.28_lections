# PostgreSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создовать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - сама база данных, она объектно реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой

# SQL (Structured Query language) - декларативный язык структурированных завпросов, он применяется для создания и получения данных при помощи запросов в БД

# -----------------------
# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа
# exit

# команда для входа в своего юзера 
# psql

# команда для выхода
# \q

# создание суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# изменение пароля
# ALTER USER 'username' WITH PASSWORD '1';

# создание бд
# CREATE DATABASE 'name';

# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы (нужно подлючиться к бд заранее)

# \d 'name' - подробная информация про таблицу (нужно подлючиться к бд заранее)

# \c 'name' - команда для подколючения к бд

# psql -U <username> -d <dbname> -подключаемся под выбранным username к dbname


# --------------------------------
# Типы полей в Postgres

# Numeric Types(числовые типы)
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # с. bigint(8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающей точкой, вещественное 
    # f. double precsion (8 bytes) -> real но только с двойной точностью
    # d. serial (4 bytes) -> integer, auto-increment

# Character types(Символьные типы(строковые)):
    # a. varchar(кол-во символов) -> если мы укажеи 50 символов, а заполним только 10, то остальные будут свободны. Макс 255
    # b. char(кол-во символов) -> если мы укажеи 50 символов, а заполним только 10, то остальные будут заполнены пробелом. Макс 255
    # с. text() -> неогр кол-во символов

# Boolen Type
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y) - (245, -12)

# enumerate types:
    # ('a', 'b', 'c')   
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad');


# ------------------
# Команда для создания таблицы
# CREATE TABLE <tableName> (
#     <column> <type>,
# )

# CREATE TABLE films (
    # code char(5),
    # title varchar(100),
    # date date,
    # genre varchar(50),
    # budget integer,
    # country varchar(50),
    # id serial
    # );

# DROP TABLE <name> - удаление таблицы

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# INSERT INTO films (code, title, date, genre, budget, country) VALUES 
# ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', 1000000, 'USA'),
# ('het5', 'Lord of The Rings', '2001-06-12', 'Fantasy', 1200000, 'USA');

# Команда для получения данных
# SELECT (columns)* FROM <table>;

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;

# ORDER BY: Позволяет нам сортировать выодящие данные по убыванию или возрастанию.  ASC(по возрастанию) и DESC(по убыванию)
# Cинтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC];

# WHERE: используется для фильтрации по полям. будут выводится только те данные которые соответсвуют условию оператора WHERE
# Cинтаксис: SELECT <row> FROM <tablename> WHERE  <row> = 'чему либо';

# BETWEEN: условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответсвует введенному шаблону для строк. Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра
# Cинтаксис: SELECT <row> FROM <tablename> WHERE  <row> LIKE/ILIKE 'чему либо';

# AND оператор и, для множетсвенных условий 
# IN: WHERE <row> in (1,2,3,4);

# LIMIT: ставит ограничение в кол-во получаемых данных

# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку. И теперь для каждой группы иожно использовать функцию

# HAVING: ставит условие при помози которого данные отбираются в группировка

# Агрегатные фукнции: AVG(), COUNT(), MIN(), MAX(), SUM()

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename>

# ----------------------------------
# Связи между таблицами(relations):
    # 1. Один к одному (One to One) - человек и паспорт
        # в одну из таблиц добавляется поле fk и дается ограничение unique
    # 2. Один ко многим (One to Many) - человек и банковские карты
        # в таблицу много (банковские карты) доб. поле fk
    # 3. Много ко многим (Many to Many) - Студенты и преподы
        # создается вспомогательная 3ья таблица со связями

# Ограничения:
    # 1. NOT NULL - обязательно к заполненинию
    # 2. UNIQUE  - то что будут хранится только уникальные данные
    # 3. CHECK -> CHECK age > -1 - ограничение проверки на условие
    # 4. PRIMARY KEY(для установки идентификатора данных в таблице)
    # 5. FOREIGN KEY(для установки связей между таблицами)
    # 6. ON DELETE - для установки поведения при удаленнии данных которые были связаны


# -----------------------------------------
# JOIN: выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id; 
# - Запрос сразу в две таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1.product_id;

# ---------------------------------------------

# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100
# SELECT source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100; 


# 2. Найти кол-во глав в каждом произведении
# select count(*), work.title from chapter join work on work.workid = chapter.workid group by work.title order by count(*) desc;

# 3. Найти сколько произведений относятся к каждому 
# select count(*), genretype from work group by genretype;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select count(*), work.title from paragraph join work on work.workid = paragraph.workid group by work.title;


# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# select character.charname, work.title, work.genretype, work.year from character_work join character on character.charid = character_work.charid join work on work.workid = character_work.workid where character.speechcount > 200 order by work.year desc;


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT character.charname, COUNT(*) AS works_count FROM character_work JOIN character
# ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid
# GROUP BY character.charname ORDER BY works_count DESC LIMIT 1;





























