import re

def part_one(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        summation = 0
        for r in data.split(","):
            l, u = re.match(r"(\d+)-(\d+)", r).groups()
            for i in range(int(l), int(u)+1):
                length = len(str(i))
                if length % 2 == 1:
                    continue
                half = length // 2
                if str(i)[:half] == str(i)[half:]:
                    summation += i
    return summation


def part_two(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        summation = 0
        for r in data.split(","):
            l, u = re.match(r"(\d+)-(\d+)", r).groups()
            for i in range(int(l), int(u)+1):
                length = len(str(i))
                for x in range(1, length//2+1):
                    if length % x != 0:
                        continue
                    #print(i, x, str(i)[:x])
                    if (str(i)[:x]*(length//x) ==  str(i)):
                        summation += i
                        print(str(i)[:x]*(length//x) , str(i))
                        break
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
