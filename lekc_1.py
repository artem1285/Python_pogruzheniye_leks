# name = 'alex'
# age = None

# a =  42
# print(id(a))
# a = 'hello world'
# print(id(a))
# print(name, age, a, 456, 'text', sep=' (=^.^=) ', end= '#')
# print('any text')
# res = input('print your text: ')
# print('ты написал ',res)

# ADULT = 18 // константа 
# age = int(input('сколько тебе лет? '))
# how_old = ADULT - age
# print(how_old, 'осталось до совершеннолетия ')
# pwd = 'text'
# res = input ('input password: ')
# if res == pwd:
#     print('доступ разрешен ')
#     print('но будьте осторожны ')
# else:
#     print('доступ запрешен ')
# print('работа завершена ')
# color = input ('твой любимый цвет: ')
# if color == 'красный':
#     print('любитель яркого')
# elif color == 'зеленый':
#     print('ты не оходтник?')
# elif color == 'синий':
#     print('ха, классика')
# else:
#     print('тебя не понять ')

# // match case // 
# match color:
#     case 'красный' | 'оранжевый':
#         print('любитель яркого')
#     case 'зеленый':
#         print('ты не оходтник?')
#     case 'синий'| 'голубой':
#         print('ха, классика')
#     case _:
#         print('тебя не понять ')
# year = int(input ('введите год в формате ууу: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 == 0:
#      print('обычный')
# else:
#     print('високосный')
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input ('Введите число: '))
# if num  not in data:
#      print('леонардо грустит')
# //
# my_math = int(input ('2 + 2 =  '))
# if 2 + 2 == my_math:
#     print('верно')
# else:
#     print('вы уверены?')

# my_math = int(input ('2 + 2 =  '))
# print('верно' if 2 + 2 == my_math else print('вы уверены?')

# // ЦИКЛЫ while
# num = float (input('Введитте число: '))
# count = 0
# while count < num:
#     print (count)
#     count +=2

# // continue 
# num = float (input('Введитте число: '))
# STEP = 2
# limit = num - STEP
# count = - STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print (count)

# // break
# min_limit = 0
# max_limit = 10
# while True:
#     print ('введите число между', min_limit, 'и' max_limit, '? ')
#     num = float (input())
#     if num < min_limit or num > max_limit:
#           print ('неверно')
#     else:
#          break     
# print ('Было введено число  ' , num)
  
# // else 

# min_limit = 0
# max_limit = 10
# count = 3
# num = None
# while count > 0:
#     print ('попытка  ', count)
#     count -= 1

#     print('введите число', min_limit, 'и', max_limit, '?')
#     num = float (input())
#     if num < min_limit or num > max_limit:
#           print ('неверно')
#     else:
#          break
# else:
#      print ('Исчерпаны все попытки, сожалею')
#      quit() 

# print ('Было введено число  ' , num)

# // for in
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#      print(item)

# // арифметический цикл, функция range() 
# num = int (input('Введитте число: '))
# for i in range (0, num, 2):
#      print(i)

# // функция enumerate() 
# animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
# for i, animal in enumerate (animals, start = 1):
#      print(i, animal)

"""
data = 0
while data < 100:
 data += 3
 if data % 40 == 0:
     break
else:
 data += 5
print(data)
"""

"""
ЛЕКЦИЯ 2
Погружение в Python (лекции)
Урок 2. Простые типы данных 
"""
"""
// Ф type, id
a = 5
print(type (a), id(a))
a = "hello wprd"
print(type (a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type (a), id(a))
"""
"""
# Ф isinstance
data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, (int, float, complex)))
"""
"""
// оператор is 
num = 2 + 2 * 2
digit = = 36 / 6 
print ( num == digit)
print (num is digit)

'''
a = 5
print (a, id(a))
a += 1
print (a, id(a))

# txt = 'hello word'
# txt [5] = '-'
txt = 'hello word'
print (txt, id(txt))
txt = txt.replace(' ', '_')
print (txt, id(txt))
'''
'''
a = c = 2
b = 3
print (a, id(a), b, id(b), c, id(c))
a = b + c
print (a, id(a), b, id(b), c, id(c))
'''
'''
# // хэш

x = 42
y = 'text'
z = 3.1415
print (hash(x), hash(y), hash(z))
my_list = [x, y, z]
print (hash(my_list))
'''
# // Аннотация типов
a: int = 42
b: float = float(input('введите число: '))
a = a / b


def my_func(data: list [int, float]) -> float:
    res = sum(data) / len(data)
    return res
print(my_func([2, 5.5/ 15, 8.0, 13.74]))

# // Использование | черты
a: int | float = 42
b: float = float(input('введите число: '))
a = a / b


# //атрибуты и методы
print('hello world!'.__doc__)
print(str.__doc__)

print('hello world!'.upper())
print('hello world!'.count('L'))

# // Функция dir, help
print(dir('hello world!'))
help('hello world!')


# //Целые числа 
x = int('42')
y = int(3.1415)
z = int('hello', base  = 30)
print (x, y , z, sep = '\n')

# // резиновый int
import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys. getsizeof(num), num)
    num *= STEP
'''

num = 7_901_123_456_789
print(num)


# // bin(x) oct(x) hex(x)
num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

# // вещественные числа
print(0.1 + 0.2)
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)

# // Логические типы 

DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по умолчанию:'))
level = num or DEFAULT
print(level)

name = input('как вас зовут?')
if name:
    print('Привет,' + name)
else:
    print('Анонимус, приветсвую' )    

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())
"""

# // строки 
# txt = 'Как называется "Война и мир".'

# class str(object):
"""
    str(object= ' ') -> str
    str(butes _or_buffer[, encoding [, errors]]) -> str
    ...
    
    # // Строки и способы их записи
text = 'Привет.Как ты, друг? Рад тебя видеть.'
print (text)

long_text = 'Первая вкладка — Ctrl + 1, вторая Ctrl + 2 и так далее. \
    Комбинация нехитрая, но не очень удобная:' \
    'пальцы человека не очень приспособлены для таких выгибонов. \
Часто проще отделить вкладку в окно и переключаться Alt + Tab'
print(long_text)

# // Конкатенация строк

LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' +\
str(100 - age) + " до ста лет, но длинна" \
" строки не должна превышать " +\
str(LIMIT) + ' символов.'
print(text)
'''
# // Размер строки в памяти

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())


# // Математика в Python

# // Модуль math

import math
print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(dir(math))
print (help(math.gcd))

# // Модуль decimal
import decimal
print(0.1 + 0.2)
pi = decimal.Decimal (3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375)
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

decimal.getcontext().prec = 120
sceince = 2 * pi * decimal.Decimal (23.452346) ** 2
print(sceince)

# //Модуль fraction
import fractions
f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

# //Комплексные числа
a = complex(2, 3)
b = complex('3+3j')
print(a, b, a == b, sep='\n')


# //Математические функции «из коробки» 
x = -42
print(abs(x))

a = 42
b = 5
print(divmod(a, b))

print(pow(a, b))
print(pow(a, b, 10))

print(round(3.141_592_653_589_793, 3))
"""

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set) 
print(f'{my_set = } \n {other_set = } \n {new_set =}')