import re


def part_one(file_path):
    with open(file_path, 'r') as file:
        solution = 0
        for line in file.read().strip().splitlines():
            line = line.split(":")[1]
            win_str, my_str = line.split(" | ")
            win_set = set(re.findall("\d+", win_str))
            my_set = set(re.findall("\d+", my_str))
            amount = len(win_set.intersection(my_set))
            if amount:
                solution += 2 ** (len(win_set.intersection(my_set)) - 1)
    return solution

def part_two(file_path):
    with open(file_path, 'r') as file:
        solution = 0
        from collections import defaultdict
        card_counts = defaultdict(int)
        for line in file.read().strip().splitlines():
            card, line = line.split(":")
            card = int(card.split()[1])
            card_counts[card] += 1

            win_str, my_str = line.split(" | ")
            win_set = set(re.findall("\d+", win_str))
            my_set = set(re.findall("\d+", my_str))
            amount = len(win_set.intersection(my_set))
            for i in range(1, amount+1):
                card_counts[card+i] += card_counts[card]
    return sum(card_counts.values())


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
