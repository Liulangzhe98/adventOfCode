from typing import List


def part_one(file_path):
    with open(file_path, 'r') as file:
        part_a, part_b = file.read().strip().split("\n\n")

        rules = [
            tuple(x.split("|")) for x in part_a.splitlines()
        ]
        count = 0
        for line in part_b.splitlines():
            spl: List = line.split(",")
            for p, n in rules:
                try:
                    if spl.index(p) < spl.index(n):
                        continue
                    else:
                        break
                except ValueError:
                    continue
            if (p, n) == rules[-1]:
                count += int(spl[len(spl)//2])
    return count


def part_two(file_path):
    with open(file_path, 'r') as file:
        part_a, part_b = file.read().strip().split("\n\n")

        rules = [
            tuple(x.split("|")) for x in part_a.splitlines()
        ]
        count = 0
        for line in part_b.splitlines():
            fixing = False
            spl: List = line.split(",")
            while True:
                for p, n in rules:
                    try:
                        if spl.index(p) < spl.index(n):
                            continue
                        else:
                            break
                    except ValueError:
                        continue
                if (p, n) != rules[-1]:
                    if not fixing:
                        print(spl)
                    fixing = True

                    temp = spl[spl.index(p)]
                    spl[spl.index(p)] = spl[spl.index(n)]
                    spl[spl.index(n)] = temp
                    continue
                if (p, n) == rules[-1]:
                    if fixing:
                        count += int(spl[len(spl) // 2])
                    break
    return count


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
    timed_print("Solution 2 ", part_two, "input.txt") # 10547 too high
    

if __name__ == "__main__":
    main()
