def part_one(file_path):
    with open(file_path, 'r') as file:
        summation = 0
        for line in file.read().strip().splitlines():
            joltage = list(line[-2:])
            for c in line[:-2][::-1]:
                for i in range(len(joltage)):
                    if c >= joltage[i]:
                        temp = joltage[i]
                        joltage[i] = c
                        c = temp
                    else:
                        break
            summation += (int("".join(joltage)))
    return summation


def part_two(file_path):
    with open(file_path, 'r') as file:
        summation = 0
        for line in file.read().strip().splitlines():
            joltage = list(line[-12:])
            for c in line[:-12][::-1]:
                for i in range(len(joltage)):
                    if c >= joltage[i]:
                        temp = joltage[i]
                        joltage[i] = c
                        c = temp
                    else:
                        break
            summation += (int("".join(joltage)))
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
