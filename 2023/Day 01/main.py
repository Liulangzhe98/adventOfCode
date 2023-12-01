import re

def part_one(file_path):
    sum_of_digits = 0
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            digits = re.findall("\d", line)
            sum_of_digits += int(digits[0] + digits[-1])
    return sum_of_digits


def part_two(file_path):
    sum_of_digits = 0
    dict_of_digits = {
            "one" : "1",
            "two" : "2",
            "three" : "3",
            "four" : "4",
            "five" : "5",
            "six" : "6",
            "seven" : "7",
            "eight" : "8",
            "nine" : "9"
            }
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            digits = []
            for key in list(dict_of_digits.keys())+["\d"]:
                for m in re.finditer(key, line):
                    digits.append(
                            (m.start(), m.group())
                            )
            sol = list(dict_of_digits.get(x[1], x[1]) for x in sorted(digits))
            sum_of_digits += int("".join((sol[0], sol[-1])))
    return sum_of_digits


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test_2.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
