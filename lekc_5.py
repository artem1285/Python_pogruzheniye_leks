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
'''
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

















