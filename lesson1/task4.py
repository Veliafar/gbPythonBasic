quarter = int(input('enter number of quarter (1-4):'))

if (1 < quarter > 4):
    print('Enter correct int')

if (quarter == 1):
    print('x > 0; y > 0')
elif (quarter == 2):
    print('x > 0; y < 0')
elif (quarter == 3):
    print('x < 0; y < 0')
elif (quarter == 4):
    print('x < 0; y > 0')        