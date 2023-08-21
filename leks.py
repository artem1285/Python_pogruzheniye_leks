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


x = int('42')
y = int(3.1415)
z = int('hello', base  = 30)
print (x, y , z, sep = '\n')

# // резиновый int
import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys. getsizeof(num), num)
    num *= STEP

    
num = 7_901_123_456_789
print(num)
 
#  // Строки и способы их записи
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

# // Размер строки в памяти

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

# // Функция len 

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print (len(my_list))
print (len(matrix))
print (len(matrix[1]))

// для само проверки 
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

# // Метод join
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
    print (f'{tuple_data[0] = } value before 100 - {100 - tuple_data [1]}')

for key, value in my_dict.items():
     print (f'{key = } value before 100 - {100 - value}')

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
err =  my_dict.pop ()


# //Метод update
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

# // МЕТОД in
my_set = {3, 4, 2, 5, 6, 1, 7}
print( 42 in my_set)

my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
print(my_set.discard(10))

# //Байты, bytes и bytearray

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
'''
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = } \n {y = }')

