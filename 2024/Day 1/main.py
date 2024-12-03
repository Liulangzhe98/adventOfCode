def part_one(file_path):
    with open(file_path, 'r') as file:
        l, r = [], []
        for line in file.read().strip().splitlines():
            f, s = line.split('  ')
            l.append(int(f.strip()))
            r.append(int(s.strip()))

        l.sort()
        r.sort()

    return sum((abs(x-y) for x, y in zip(l, r)))


def part_two(file_path):
    with open(file_path, 'r') as file:
        l, r = [], []
        for line in file.read().strip().splitlines():
            f, s = line.split('  ')
            l.append(int(f.strip()))
            r.append(int(s.strip()))
    return sum(x*r.count(x) for x in l)


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
