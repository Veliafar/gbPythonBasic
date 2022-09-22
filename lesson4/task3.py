# Задайте последовательность чисел.
#  Напишите программу,
#  которая выведет список
#  неповторяющихся элементов исходной
#  последовательности.

test_data = [
    [[1, 2, 2, 3, 4, 5, 5, 7, 4, 7, 6, 7, 10, 10], [1, 2, 3, 4, 5, 6, 7, 10]]
]

def removeRepeatedElemFromList(listFromUser):
    return list(set(listFromUser))

for listFromUser, expected_value in test_data:
    assert removeRepeatedElemFromList(listFromUser) == expected_value