# Задайте натуральное число N. 
# Напишите программу,
#  которая составит список простых множителей числа N.

N = 98

def multiplier(number):
    multiplier_list = []
    i = 2 
    while i <= number:
        if number % i == 0:
            multiplier_list.append(i)
            number //= i
            i = 2
        else:
            i += 1
    return multiplier_list

print(multiplier(N))