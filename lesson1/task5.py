import math

print("\nEnter coordiantes of two points to view distance.\n")

x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

d = math.sqrt(math.pow((y1 - x1), 2) + math.pow((y2 - x2), 2))

print('distance: ', round(d, 2));