from collections import defaultdict
import re
from functools import reduce

def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def solve_problem(op, math_problem):
    match op:
        case '*':
            return reduce(lambda x, y: int(x) * int(y), math_problem) 
        case '+':
            return reduce(lambda x, y: int(x) + int(y), math_problem) 

def part_one(file_path):
    with open(file_path, 'r') as file:
        data = [] 
        for line in file.read().strip().splitlines():
            tokens = re.split(r'\s+', line.strip())
            data.append(tokens)
        data = trans(data)

        summation = 0
        for math_problem in data:
            op = math_problem.pop(-1)
            summation += solve_problem(op, math_problem)
    return summation


def part_two(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.read().splitlines():
            data.append(list(line))
        data = trans(data)
        
        process = []
        summation = 0
        for e, math_problem in enumerate(data):
            if "".join(math_problem).strip() == "" or e == len(data) - 1:
                if e == len(data) - 1:
                    process.append(math_problem)
                op = process[0][-1]
                a = ([int("".join(l[:-1])) for l in process])                
                summation += solve_problem(op, a)
                process = []
            else:
                process.append(math_problem)
    
    return summation


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
