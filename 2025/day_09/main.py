from itertools import combinations
def part_one(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.read().strip().splitlines():
            data.append(tuple(int(x) for x in line.split(',')))

        max_rect = 0
        for a, b in combinations(data, 2):
            max_rect = max(max_rect, (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1))
    return max_rect

from shapely.geometry import Point
from shapely.geometry import Polygon

def part_two(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.read().strip().splitlines():
            data.append([int(x) for x in line.split(',')])
        polygon = Polygon(data)

        max_rect = 0
        for a, b in combinations(data, 2):
            c1 = [a[0], b[1]]
            c2 = [b[0], a[1]]
            if polygon.contains(Polygon([a, c1, b, c2])):
                max_rect = max(max_rect, (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1))
    return max_rect

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
