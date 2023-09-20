'''
# однострочники
a = 42
b = 73
a, b = b, a
print(f'{a = } \ t {b = }')

# Распаковка
a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')

a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')

a, b, c = {"один", "два", "три", "четыре", "пять"}
print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack(expected 3)

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",
]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link ='https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')

data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')
print()

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

# Множественное присваивание и сравнение 
# хорошо
a = b = c = 0   
a += 42
print(f'{a=} {b=} {c=}')

# плохо
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')

# обмен переменных местами
a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')

# множественное сравнение
a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')

if a < b < c:
    print('b больше a и меньше c')

#  Итераторы 

# Функция iter() 
a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

# дома
# Переменная sentinel

data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must becallable

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()

# Функция next()
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter)) # StopIteration

# Значение дефолт
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))

# самопроверка
data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)
'''

# Генераторы
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')

b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')


# Генераторные выражения

my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at0x000001ED58DD7D60>
for char in my_gen:
    print(char)

# сложный объект
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

# List comprehensions 
my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
        if item % 2 == 0:
            res.append(item)
print(f'{res = }')

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')


# Пример генерации множеств
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')

#  Генерация словарей

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')

# Самопроверка

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)

# Как создавать свои собственные генераторы
# Используя зарезервированное слово def 

# Обычная Ф

def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

#  Команда yield . Ф превратилась в генератор

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')
'''
# Функции iter и next для генераторов
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # StopIteration


#  самопроверка
def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)

for item in gen(10, 1):
    print(f'{item = }')


