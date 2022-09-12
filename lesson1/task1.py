day = int(input('Введите номер дня недели (1 - 7): '))

if (day < 0 or day > 7):
    print('Введите верное число')
    exit()

if (day >= 1 and day <= 5):
    print('будний день')
elif (day == 6 or day == 7):
    print('выходной')

