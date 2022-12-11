# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:

# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]


import random
number = int(input('Введите число N: '))
new_number = []
for i in range(number):
    new_number.append(random.randint(-50, 50))
print(f'массив {new_number}')
i = 0
for j in new_number:
    i = i + 1
    if j < 0:
        new_number.insert(i, 0)
print(f'получили массив  ->  {new_number}')