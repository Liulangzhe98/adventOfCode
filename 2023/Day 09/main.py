from itertools import pairwise

def solve_recursion(history: list) -> int:
    if history.count(0) == len(history):
        return 0
    next_list = [y-x for x,y in pairwise(history)]
    return history[-1] + solve_recursion(next_list)


def solve_recursion_part_two(history: list) -> int:
    if history.count(0) == len(history):
        return 0
    next_list = [y-x for x,y in pairwise(history)]
    return history[0] - solve_recursion_part_two(next_list)

def part_one(file_path):
    with open(file_path, 'r') as file:
        solution = 0
        for line in file.read().strip().splitlines():
            data = [int(x) for x in line.split()]
            solution += solve_recursion(data)
    return solution


def part_two(file_path):
    with open(file_path, 'r') as file:
        solution = 0
        for line in file.read().strip().splitlines():
            data = [int(x) for x in line.split()]
            solution += solve_recursion_part_two(data)
    return solution


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
