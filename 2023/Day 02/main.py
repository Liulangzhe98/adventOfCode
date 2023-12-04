import math
import re

def part_one(file_path):
    max_rgb = {
            "red": 12,
            "green": 13,
            "blue": 14,
            }
    solution = 0
    with open(file_path, 'r') as file:
        for e, line in enumerate(file.read().strip().splitlines(), 1):
            pairs = re.findall("(\d+) (red|green|blue)", line)
            if all((int(x) <= max_rgb[y] for x, y in pairs)):
                solution += e
    return solution


def part_two(file_path):
    with open(file_path, 'r') as file:
        solution = 0
        for line in file.read().strip().splitlines():
            pairs = re.findall("(\d+) (red|green|blue)", line)
            max_rgb = [0, 0, 0]
            for pair in pairs:
                match pair[1]:
                    case "red":
                        max_rgb[0] = max(max_rgb[0], int(pair[0]))
                    case "green":
                        max_rgb[1] = max(max_rgb[1], int(pair[0]))
                    case "blue":
                        max_rgb[2] = max(max_rgb[2], int(pair[0]))
            solution += math.prod(max_rgb)
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
