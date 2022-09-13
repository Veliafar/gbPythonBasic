# Реализуйте алгоритм перемешивания списка.+ 3

import random

num = int(input('Введите число: '))

numbers = list(range(num))

random_numbers = []

for i in range(num):
    random_index = random.randint(0, len(numbers)-1)
    random_num = numbers.pop(random_index)
    print(random_num, end=', ')