# Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def print_poly(coeff):
    n = len(coeff)
    for i in range(n):
        print(coeff[i], end="")
        if i != 0:
            print("x^", i , end="", sep="")
        if i != n -1:
            print(" + ", end="")


randomlist = []

for i in range(0,5):
    n = random.randint(1,100)
    randomlist.append(n)

print_poly(randomlist)