import re


def part_one(file_path):
    with open(file_path, 'r') as file:
        output = 0
        for line in file.read().strip().splitlines():
            results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
            output += sum((int(x) * int(y) for x, y in results))
    return output


def part_two(file_path):
    with open(file_path, 'r') as file:
        flag = True
        output = 0
        for line in file.read().strip().splitlines():
            results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)|(do)\(\)", line)
            for x, y, f, t in results:
                if f:
                    flag = False
                elif t:
                    flag = True
                elif flag:
                    output += int(x) * int(y)
    return output


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
