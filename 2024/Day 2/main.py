from itertools import combinations


def is_report_save(report):
    runs = zip(report, report[1:])
    check = [x - y for x, y in runs]
    return (
            all((1 <= abs(x) <= 3 for x in check))
            and (all((x >= 0 for x in check)) or all((x < 0 for x in check)))
    )


def part_one(file_path):
    with open(file_path, 'r') as file:
        safe = 0
        for line in file.read().strip().splitlines():
            safe += int(is_report_save([int(x.strip()) for x in line.split()]))
    return safe


def part_two(file_path):
    with open(file_path, 'r') as file:
        safe = 0
        for line in file.read().strip().splitlines():
            report = [int(x.strip()) for x in line.split()]
            safe += any((is_report_save(x) for x in combinations(report, len(report)-1)))
    return safe


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
