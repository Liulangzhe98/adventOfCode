from itertools import zip_longest
from functools import cmp_to_key


def int_check(a, b):
    # Same as the sign check of day 9 but now with b being variable instead of 0
    return (a > b) - (a<b)


def logic(lhs, rhs):
    for e, (a, b), in enumerate(zip_longest(lhs, rhs, fillvalue=None), 1):
        if a == None:
            return -1
        if b == None:
            return 1

        if type(a) == int and type(b) == int:
            result = int_check(a, b)
        elif type(a) == list and type(b) == list:
            result = logic(a, b)
        elif type(a) != list:
            result = logic([a], b)
        elif type(b) != list:
            result = logic(a, [b])

        if result == 0:
            continue
        return result
    return 0



def part_one(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        for pair in file.read().split("\n\n"):
            lhs, rhs = pair.split("\n")
            pairs.append((eval(lhs), eval(rhs)))
    return sum(
        [e for e, (lhs, rhs) in enumerate(pairs, 1) if logic(lhs, rhs)*-1 == 1])


def part_two(file_path):
    A = [[2]]
    B = [[6]]

    packets = []
    with open(file_path, 'r') as file:
        for pair in file.read().split("\n\n"):
            lhs, rhs = pair.split()
            packets.extend([eval(lhs), eval(rhs)])
    packets.extend([A, B])
    packets.sort(key=cmp_to_key(logic))
    return (packets.index(A)+1)*(packets.index(B)+1)


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")

    
if __name__ == "__main__":
    main()
