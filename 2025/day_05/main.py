import re
from itertools import combinations

def part_one(file_path):
    with open(file_path, 'r') as file:
        fresh, available = file.read().strip().split("\n\n")
        ranges = []
        for line in fresh.splitlines():
            l, u = re.match(r"(\d+)-(\d+)", line).groups()
            ranges.append((int(l), int(u)))
        summation = 0
        for x in available.splitlines():
            x = int(x)
            for r in ranges:
                if x >= r[0] and x <= r[1]:
                    summation += 1
                    break
    return summation

def any_overlap(data):
    for (min1, max1), (min2, max2) in combinations(data, 2):
        if min1 > max2 or max1 < min2:
            continue
        else:
            return (min1, max1), (min2, max2)
    return None

def part_two(file_path):
    with open(file_path, 'r') as file:
        fresh, _ = file.read().strip().split("\n\n")
        ranges = []
        for line in fresh.splitlines():
            l, u = re.match(r"(\d+)-(\d+)", line).groups()
            ranges.append((int(l), int(u)))
        while True:
            if not (a:= any_overlap(ranges)):
                return sum([b-a+1 for a, b in ranges])
            ranges.remove(a[0])
            ranges.remove(a[1])

            item_values = a[0] + a[1]
            ranges.append((min(item_values), max(item_values)))
    return None

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
