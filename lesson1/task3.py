print('\nEnter X and Y and you will get num of quarter (X and Y != 0)\n')
X = int(input('X: '))
Y = int(input('Y: '))

if (X == 0 or Y == 0):
    print('Enter correct int')

if (X > 0 and Y > 0):
    print('quarter 1')
elif (X > 0 and Y < 0):
    print('quarter 2')
elif (X < 0 and Y < 0):
    print('quarter 3')
elif (X < 0 and Y > 0):
    print('quarter 4')        