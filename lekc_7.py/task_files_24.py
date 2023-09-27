# пример с переменной 
size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))

# самопроверка
start = 10
stop = 100
with open('data.bin', 'bw+') as f:
    for i in range(start, stop + 1):
        f.write(str(i).encode('utf-8'))
        if i % 3 == 0:
            f.seek(-2, 1)
    f.truncate(stop)
    f.seek(0)
    res = f.read(start)
    print(res.decode('utf-8'))