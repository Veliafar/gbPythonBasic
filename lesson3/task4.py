# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


test_data = [
    [45, '101101'],
    [3, '11'],
    [2, '10']
]


def decadeToBinary(num: int) -> str:
    string = ''

    while num:    
        string = str(num % 2) + string
        num //= 2

    return string


for list, expected in test_data:
    assert decadeToBinary(list) == expected