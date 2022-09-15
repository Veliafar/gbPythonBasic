# Напишите программу, которая найдёт произведение
#  пар чисел списка. Парой считаем первый 
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


test_data = [
    [[2, 3, 4, 5, 6], [12, 15, 16]],
    [[2, 3, 5, 6], [12, 15]],    
]


def calc_pair_multiply(list):
    i, j = 0, len(list) - 1
    
    result = []

    while i <= j:
        result.append(list[i] * list[j])
        i = i + 1
        j = j - 1        


    print(result)

    return result
    



for list, expected in test_data:
    assert calc_pair_multiply(list) == expected