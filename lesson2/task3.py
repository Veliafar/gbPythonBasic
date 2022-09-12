# Задайте список из n чисел последовательности
#  Sn = (Sn-1 + 3) и выведите на экран их сумму.
# ссылка на формулу https://disk.yandex.ru/i/smKmpgtfQv4lIA

#  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input('Введите число: '))

sequence = {
    1: 4
}

for i in range(2, num+1):
    sequence[i] = sequence[i-1] + 3

print(sequence)