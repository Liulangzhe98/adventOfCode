import re


def part_one(file_path):
    with open(file_path, 'r') as file:
        obstacles = []
        for e, line in enumerate(file.read().strip().splitlines(), 1):
            for m in re.finditer('#', line):
                obstacles.append((e, m.start()+1))
            if "^" in line:
                pos = line.index("^")
                guard = [e, pos+1, 0]
        visited = set(tuple(guard[:2]))
        while True:
            try:
                if guard[2] == 0:
                    in_line = list(filter(lambda x: x[1] == guard[1], obstacles))
                    in_line.sort(key=lambda x: x[0], reverse=True)

                    first_in_line = next(filter(lambda x: x[0] < guard[0], in_line))
                    steps = set(((y, guard[1]) for y in range(guard[0], first_in_line[0], -1)))
                    guard[0] = first_in_line[0] + 1
                    guard[2] = (guard[2] + 1) % 4

                if guard[2] == 1:
                    in_line = list(filter(lambda x: x[0] == guard[0], obstacles))
                    in_line.sort(key=lambda x: x[1], reverse=False)
                    first_in_line = next(filter(lambda x: x[1] > guard[1], in_line))
                    steps |= set(((guard[0], x) for x in range(guard[1], first_in_line[1])))
                    guard[1] = first_in_line[1] - 1
                    guard[2] = (guard[2] + 1) % 4
                if guard[2] == 2:
                    in_line = list(filter(lambda x: x[1] == guard[1], obstacles))
                    in_line.sort(key=lambda x: x[0], reverse=False)
                    first_in_line = next(filter(lambda x: x[0] > guard[0], in_line))
                    steps |= set(((y, guard[1]) for y in range(guard[0], first_in_line[0])))
                    guard[0] = first_in_line[0] - 1
                    guard[2] = (guard[2] + 1) % 4
                if guard[2] == 3:
                    in_line = list(filter(lambda x: x[0] == guard[0], obstacles))
                    in_line.sort(key=lambda x: x[1], reverse=True)
                    first_in_line = next(filter(lambda x: x[1] < guard[1], in_line))
                    visited |= set(((guard[0], x) for x in range(guard[1], first_in_line[1], -1)))
                    guard[1] = first_in_line[1] + 1
                    guard[2] = (guard[2] + 1) % 4
                visited |= steps
            except StopIteration:
                visited |= steps
                if guard[2] == 3:
                    visited |= set(((guard[0], x) for x in range(guard[1], 1, -1)))
                break
    return len(visited)-1


def part_two(file_path):
    with open(file_path, 'r') as file:
        obstacles = []
        for e, line in enumerate(file.read().strip().splitlines(), 1):
            for m in re.finditer('#', line):
                obstacles.append((e, m.start() + 1))
            if "^" in line:
                pos = line.index("^")
                guard = [e, pos + 1, 0]

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
    # timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
