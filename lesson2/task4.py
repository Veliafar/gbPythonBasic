# Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

num = 20

numbers = []
for i in range(-num, num+1):
    numbers.append(i)

print(numbers)

file = open("file.txt", encoding="utf-8")
indexes = []

for line in file:
    print(line.strip())
    
