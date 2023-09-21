'''
# import

import sys
print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

import random

print(random.randint(1, 6))

# from
from sys import builtin_module_names, path
print(builtin_module_names)
print(*path, sep='\n')

# as
import random as rnd
from sys import builtin_module_names as bmn, path as p
print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
print(path) # NameError: name 'path' is not defined
print(sys.path) # NameError: name 'sys' is not defined

# Плохой импорт со звесдочкой

from random import randint

__all__ = ['func', '_secret']

SIZE = 100

_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z

result = func(1, 6)
'''

#  Виды модулей
"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.

_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1

def add(*args):
    res = _START_SUM
    for item in args:
        res += item
    return res

def sub(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res -= item
    return res

def mul(*args):
    res = _START_MULT
    for item in args:
        res *= item
    return res

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res /= item
    return res

print(f'{add(2, 4) = }')
print(f'{add(2, 4, 6, 8) = }')
print(f'{sub(10, 2) = }')
print(f'{mul(2, 2, 2, 2, 2) = }')
print(f'{div(-100, 5, -2) = }')

# простой импорт
from mathematical import lekc_6_baz
x = lekc_6_baz.div (10, 2)
print (x)


# Абсольютный импорт 

from mathematical import lekc_6_baz as bm
from mathematical.lekc_6_pacet import exp
x = bm.div(12, 5)
z = exp(2, 3)
print (x, z)


# Модули “из коробки”
# Модуль sys 
print('start') 
print('stop') 
"""

# Модуль random


























