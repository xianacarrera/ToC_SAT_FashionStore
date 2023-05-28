from z3 import *
from fashion_options import Clothes, Colors
import time
import main

def create_vars(k):
    global Clothes, Colors

    # Add k garments to the Clothes dictionary
    for i in range(k):
        Clothes[f'garment{i}'] = Bool(f'garment{i}')
    # Add k colors to the Colors dictionary
    for i in range(k): 
        Colors[f'color{i}'] = Bool(f'color{i}')

    return clothes_copy, colors_copy

def create_input(k):
    with open('tests/performance.txt', 'w') as f:
        for i in range(k):
            f.write(f'garment{i}, color{i}\n')
        f.close()

if __name__ == '__main__':
    n = 1
    
    # Make a copy of the dictionaries
    clothes_copy = Clothes.copy()
    colors_copy = Colors.copy()

    options = {
        "verbose": False,
        "possible_solution": False,
        "statistics": True
    }
    
    results = []
    for n in [1, 10, 100, 1000, 5000, 10000, 50000, 100000, 200000, 1000000]:
        clothes_copy, colors_copy = create_vars(n)
        create_input(n)
        time0 = time.time()
        main.run('tests/performance.txt', options)
        time1 = time.time()
        diff = time1 - time0
        results.append(diff)
        print(f'Time for {n} extra garments and colors: {diff}')

    with open('performance_results.txt', 'w') as f:
        for i in range(len(results)):
            f.write(f'{i}, {results[i]}\n')
        f.close()

    Clothes = clothes_copy
    Colors = colors_copy