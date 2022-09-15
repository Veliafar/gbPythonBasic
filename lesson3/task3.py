# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



test_data = [
    [[1.1, 1.2, 3.1, 5, 10.01], 0.19]
]

def diff_between_min_max_fractional_part(list: list) -> float:
    max_fractional_part = float('-inf')
    min_fractional_part = float('inf')

    for num in list:
        fraction = round(num % 1, 5)

        if fraction == 0:
            continue

        if fraction > max_fractional_part:
            max_fractional_part = fraction      

        if fraction < min_fractional_part:
            min_fractional_part = fraction      

    return max_fractional_part - min_fractional_part


for list, expected in test_data:
    assert diff_between_min_max_fractional_part(list) == expected
