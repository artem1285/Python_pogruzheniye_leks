'''
a = 42
print(type(a), id (a))
print(type(id))

# very_bad_programming_style = sum
# print(very_bad_programming_style [1,2,3])

#  слово def
def my_func():
    pass

# слово pass

if a != 5:  если значение А не равно 5 
    pass          тогда ничего  неделаем, т.е мы сказали что нужен вложенный код иначе получим ошибку, но делать ничего не надо
else: a += 1  иначе прибавляем единицу 


if a == 5: если а  равно 5 
 a += 1  тогда А увеличиваем на 1 
    else: 
pass в противном случае делать ничего не надо

# В пайтон можно не писать обязательные слова if и else. отличный вариант 

if a == 5: 
a += 1 

# Аргументы функции

def quadratic_equations(a: int | float, b: int | float, c: int |
float) -> tuple[float, float] | float | str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'
print(quadratic_equations(2, -3, -9))

# Изменяемые и неизменяемые аргументы

def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') # Для демонстрации работы, но не для привычки принтить из функции
    return a

a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

# Когда используем изменяемые переменные

def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
    return data

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')

# Возврат значения из функции, return
def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *a)
    if d == 0:
        return -b / (2 * a)
    return None
print(quadratic_equations(2, -3, -9))

# Неявный return 
def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')

# Значения по умолчанию

def quadratic_equations(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *a)
    if d == 0:
        return -b / (2 * a)
print(quadratic_equations(2, -9))

# В качестве значений по умолчаний используются только неизменяемые типы данных

def from_one_to_n(n, data=None):
    if data is None:
            data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

# Позиционные и ключевые параметры
# Пример обычной функции:

def standard_arg(arg):
    print(arg) # Принтим для примера, а не для привычки
standard_arg(42)
standard_arg(arg=42)

#  /
def pos_only_arg(arg, /):
    print(arg) # Принтим для примера, а не для привычки
pos_only_arg(42)
pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
'''
# *
def kwd_only_arg(*, arg):
    print(arg) # Принтим для примера, а не для привычки
kwd_only_arg(42)
kwd_only_arg(arg=42)










