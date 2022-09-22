# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

test_data = [
    [0.001, 3.141],
    [0.1, 3.1],
    [0.0000000001, 3.1415916535],
]

def show_pi(precision: float) -> float: 

    try:
        precision = len(str(precision).split('.')[1])
    except:
        precision = int(str(precision).split('-')[1])
    
    k = 1        
    pi = 0
    for i in range(1000000):        
        if i % 2 == 0:
            pi += 4/k
        else:                
            pi -= 4/k    
        k += 2  
    
    print('\n')
    print('pi: ', pi)
    print('precision: ', precision)    
    result = float(pi)*(1 * 10 ** precision)//1/(1 * 10 ** precision)
    print('result: ', result, '\n')    
    return result 

for precision, expected_value in test_data:
    assert show_pi(precision) == expected_value