# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))

factorials = [1]

for i in range(2, num + 1):    
    next_fact = factorials[-1] * i    
    factorials.append(next_fact)
    

print(factorials)