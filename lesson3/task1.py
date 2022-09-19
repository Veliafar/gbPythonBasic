# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму
#  элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def find_elements_sum_in_odd_position(list):
    sum = 0
    for i, n in enumerate(list):
        if i % 2 != 0:
            sum += n
            
    return sum

test_data = [
    [[3,5,6,7], 12],
    [[2,3,4], 3],
    [[1,2,3,4], 6]
]

for list, expected in test_data:
    assert find_elements_sum_in_odd_position(list) == expected