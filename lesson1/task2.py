
print('check is ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z');

X = bool(input('X: '))
Y = bool(input('Y: '))
Z = bool(input('Z: '))

leftPart = not(X or Y or Z);
rightPart = not X and not Y and not Z;

if (leftPart == rightPart):
    print('equal')
else:  
    print('not equal')
    
