def part_one(file_path):
    dial = 50
    count = 0
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            a = list(line) 
            direction = a[0]
            amount = int("".join(a[1:]))
            if direction == "R":
                dial = (dial + amount) % 100
            else:
                dial = (dial - amount) % 100
            if dial == 0:
                count += 1
    return count


def part_two(file_path):
    dial = 50
    count = 0
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            a = list(line) 
            direction = a[0]
            amount = int("".join(a[1:]))
            for i in range(amount):
                if direction == "R":
                    dial += 1
                else:
                    dial -= 1
                dial = dial % 100
                if dial == 0:
                    count += 1
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
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
