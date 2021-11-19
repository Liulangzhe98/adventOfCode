# (r, c) counting from 1
# (3, 4) == 19
# (8, 8) == 98
# (8, 9) == 113 
# (2947, 3029) == ???? # input

from functools import reduce

def print_Square(size=10):
    totalList = []
    
    a = list(range(1, size))
    summation = 1
    print(f"{'|':>5} ", end="")
    [print(f"{x:3}|", end="") for x in range(1,size+1)]
    print()
    for x in a:
        curr = summation
        print(f"{x:3} | {curr:3}", end="")
        for y in list(range(x+1, x+size)):
            curr += y
            print(f"|{curr:3}", end ="")
        summation += x
        print()

import time

print_Square()

def find_number(row, col):
    return sum(list(range(1, row))) + 1 + sum(list(range(row+1, row+col)))
    
print(f"The magic square = {find_number(3, 4)}") # 19
print(f"The magic square = {find_number(2947, 3029)}") # my input number

def brute_force(number=19):
    # (3, 4) = 7981243  (test value from the known square)
    M = 252533 
    mod = 33554393
    start = 20151125
    curr = start
    
    for _ in range(number-1):
        curr = (curr *M )%mod
    print(curr)

brute_force(find_number(2947, 3029))

