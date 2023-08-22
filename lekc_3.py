"""
list_1 = list()
list_2 = list((3.14, True, 'Hello world'))
list_3 = []
list_4 = [3.14, True, 'Hello world']

my_list = [2, 4, 6, 8, 12]
print(my_list[0])
# print(my_list[6])

print(my_list[-1])
print(my_list[-10])

// метод .append
a = 42
b = 'Hello world'
c = [1, 3, 5, 7]
my_list = [None ]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)

my_list.append(my_list)
print(my_list)

# // метод extend
a = 42
b = 'Hello world'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a)
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)

my_list.extend(my_list)
print(my_list)

# // Метод pop
my_list = [2, 4, 6, 8, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10)

# //Метод count
my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.count(2)
print(spam)
eggs = my_list.count(3)
print(eggs)

# //Метод index
my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90)
print(eggs)
err = my_list.index(3)

# // Метод insert
my_list = [2, 4, 6, 8, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73)
print(my_list)

# // Метод remove
my_list = [2, 4, 6, 8, 12, ]
my_list.remove(6)
print(my_list)
my_list.remove(3)
print(my_list)

# // Сортировки и развороты
 # //Функция sorted
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')

# //Метод sort()
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# //разворот
# // Функция reversed
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)

res_list = list(reversed(my_list))
print(res_list)

for item in reversed(my_list):
    print(item)

# //Метод reverse
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

# //Синтаксический сахар [::-1]

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list [:: - 1]
print(my_list, new_list, sep= '\n')

# //срезы
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])

# //Метод copy
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep= '\n')
new_list [2] = 555
print(my_list, new_list, sep= '\n')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep= '\n')
my_list[2] = 555
print(my_list, new_list, sep= '\n')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m  = matrix.copy()
print(matrix, new_m , sep= '\n')
matrix[0] [1]= 555
print(matrix, new_m , sep= '\n')

# // import copy
import copy
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m  = copy.deepcopy(matrix)
print(matrix, new_m , sep= '\n')
matrix[0] [1]= 555
print(matrix, new_m , sep= '\n')

# // Функция len

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print (len(my_list))
print (len(matrix))
print (len(matrix[1]))

# // для само проверки
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])
print(my_list.pop())
print(my_list.extend([314, 42]))
print(my_list.sort(reverse=False))
print(my_list)

# // Строки, str
text = 'Hello world'
print(text [6])
print(text [3:7])

next_txt = text. replace ('l', "L", 2)
print(text, next_txt, sep='\n')

# // методы
text = 'Hello world'
print(text.count ('l'))
print(text.index ('l'))
print(text.find ('l'))
print(text.find ('z'))

text = 'Hello world'
print(text[::-1])

# //Форматирование строк

// символ %
name = 'Alex'
age = 12
text = "Меня зовут %s и мне %d лет " % (name, age)
print(text)

//Метод format
name = 'Alex'
age = 12
text = "Меня зовут {} и мне {} лет " .format (name, age)
print(text)

# // f-строка
name = 'Alex'
age = 12
text = f"Меня зовут {name} и мне {age} лет "
print(text)

print(f'{{Фигурные скобки}} и {name}')

pi = 3.1415
print(f'число Пи с точностью до два знака: {pi:.2f}')

data = [3254, 465499559, 75656246, 5644, 423366, 1486]
for item in data:
    print(f'{item: > 10}')

num = 2 * pi * data[1]
print(f'{num = :_}')

# //Строковые методы
# // Метод split
link = 'https://gb.ru/lessons/355973'
urls = link.split('/')
print(urls)

a, b, c = input('введите 3 числа  через пробел: ').split()
print (a, b, c)

a, b, c, *_= input('введите  не менее 3 чисел  через пробел: ').split()

# //Метод join
data = ['https:', '', 'gb.ru', 'lessons', '355973']
url = '/'.join(data)
print(url)

# // методы которые изменяет строку
# // Метод upper(), lower(), title(), capitalize()
text = 'однажды В СИУДЕНУЮ зимнЮЮ ПоРУ'
print(text.upper ())
print(text.lower ())
print(text.title ())
print(text.capitalize ())

# // Метод startswith() и endswith()
text = 'Однажды В студеную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

# // для самопроверки
text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text = :>25}')


# //Кортежи, tuple
a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1,
c2, d, sep='\n')

# //для самопроверки
my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))

# // Словари, dict

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world !'}
b = dict(one=42, two=3.14, ten='Hello world !')
c = dict([('one', 42), ('two', 3.14),  ('ten', 'Hello world !')])
print( a == b == c)

# // если надо добавить в словарь какой то элемент
my_dict = {'one': 1,'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict ['ten'] = x
print(my_dict)


# //доступ к значению словаря
TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

print(my_dict['two'])
print(my_dict[TEN])
print(my_dict[1])

# //или метод get
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))


# // Работа со словарями - МЕТОДЫ
# // Метод setdefault
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault ('five')
print(f'{spam = } \ t {my_dict=}')
eggs = my_dict.setdefault ('six', 6)
print(f'{eggs = } \ t {my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam = } \ t {my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs = } \ t {my_dict=}')


#//Метод key
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())

for key in my_dict.keys():
    print(key)

# //Метод values
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())

for value in my_dict.values():
print(value)

# //Метод items
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items():
    print(tuple_data)
print(f'{tuple_data[0] = } value before 100 - {100 - tuple_data[1]}')

for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

# //Метод popitem
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem ()
print(f'{spam = } \ t {my_dict=}')
eggs = my_dict.popitem ()
print(f'{eggs = } \ t {my_dict=}')

# //Метод pop
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop ('two')
print(f'{spam = } \ t {my_dict=}')
# err = my_dict.pop ('six')
err =  my_dict.pop ()

# //Метод update
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

#  //Для самопроверки
my_dict = {'one': 1,
 'two': 2,
 'three': 3,
 'four': 4,
 'ten': 10,
 }
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)

# //Множества, set и frozenset
# //Изменяемое множество set
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)
not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']}

# //Работа с множествами  - МЕТОДЫ
# //Метод add
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10)
my_set.add((9, 10))
print(my_set)

# //Метод remove
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)
my_set.remove(10)

# //Метод discard
my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)

# //Метод intersection
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = } \n {other_set = } \n {new_set =}')

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = } \n {other_set = } \n {new_set =}')

# //Метод union
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = } \n {other_set = } \n {new_set =}')

new_set_2 = my_set | other_set
print(f'{my_set = } \n {other_set = } \n {new_set =}')

# //Метод difference
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = } \n {other_set = } \n {new_set =}')

new_set_2 = my_set | other_set
print(f'{my_set = } \n {other_set = } \n {new_set =}')

# //МЕТОД in
my_set = {3, 4, 2, 5, 6, 1, 7}
print( 42 in my_set)

# //Для самопроверки
my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
print(my_set.discard(10))

# //Байты, bytes и bytearray
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = } \n {y = }')
"""