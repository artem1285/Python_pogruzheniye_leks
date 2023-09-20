'''
def randint(*args):
    return 'Не то, что вы искали!'


from lekc_6 import *

SIZE = 49.5
print(f'{SIZE = }\n{result = }')
# print(f'{z = }') # NameError: name 'z' is not defined
print(f'{_secret = }') # NameError: name '_secret' is not defined
print(f'{func(100, 200) = }\n{randint(10, 20) = }')

def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')
'''

import lekc_6

x = lekc_6.mul # Плохой приём
y = lekc_6._START_MULT # Очень плохой приём
z = lekc_6.sub(73, 42)
print(x(2, 3))
print(y)
print(z)









