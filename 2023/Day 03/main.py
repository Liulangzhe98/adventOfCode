import math
import re
from collections import defaultdict

def get_bounding_box(current_row ,current_col, length):
    bounding = [(current_row, current_col-1), (current_row, current_col+length)]
    for i in range(current_col-1, current_col+length+1):
        bounding.append((current_row-1, i))
        bounding.append((current_row+1, i))
    return bounding

def part_one(file_path):
    with open(file_path, 'r') as file:
        numbers = []
        symbols = []

        for e, line in enumerate(file.read().strip().splitlines()):
            results = re.finditer("(\d+|[^\d.\s]+)", line)
            for result in results:
                match result[0].isdigit():
                    case True:
                        numbers.append((e, result.start(), len(result[0]), int(result[0])))
                    case False:
                        symbols.append((e, result.start()))
    solution = 0
    for number in numbers:
        bounding = get_bounding_box(number[0], number[1], number[2])
        for row, col in bounding:
            if (row, col) in symbols:
                solution += number[3]
                break
    return solution


def part_two(file_path):
    with open(file_path, 'r') as file:
        numbers = []
        symbols = []
        
        for e, line in enumerate(file.read().strip().splitlines()):
            results = re.finditer("(\d+|\*+)", line)
            for result in results:
                match result[0].isdigit():
                    case True:
                        numbers.append((e, result.start(), len(result[0]), int(result[0])))
                    case False:
                        symbols.append((e, result.start()))
    solution = 0
    visited = defaultdict(list)
    for number in numbers:
        bounding = get_bounding_box(number[0], number[1], number[2])
        for row, col in bounding:
            if (row, col) in symbols:
               visited[f"({row}, {col})"].append(number[3]) 
               break
    return sum((math.prod(x) for x in filter(lambda x: len(x) == 2, visited.values())))


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
