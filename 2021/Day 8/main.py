import statistics
import re
import string

DEFINE_A = 97
DEFINE_G = 103

def diff_string(str1, str2, str3= ""): # str2 has to be longer or equal
    return [c for c in str2 if c not in str1+str3]


def diff_pattern(wires):
    amount = len(wires)
    segs = "".join(wires)
    counter = [(x, segs.count(x)) for x in string.ascii_lowercase[:7]]
    counter = list(filter(lambda x: x[1] < amount, counter))
    return counter


def part_one(init_vars):
    counter = 0
    for _, b in init_vars:
        counter += sum([len(x) in [2, 3, 4, 7] for x in b.split()])
    print("(1) In the output values, how many times do digits 1, 4, 7, or 8 appear?")
    print(f"Answer: {counter}")

def part_two(init_vars):
    idx_dict = [
        [0, 1, 2, 4, 5, 6],
        [2, 5],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 5, 6],
        [1, 2, 3, 5],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 4, 5, 6],
        [0, 2, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]
    ]
    mega_sum = 0
    for wires, output in init_vars:
        segments = [""]*7 # Top, left, right, middle, botleft, botright, bottom
        wires = sorted(wires.split(), key=lambda x: len(x))

     
        diff_6 = diff_pattern(wires[6:9])
        diff_6_str = "".join([x[0] for x in diff_6])
        diff_5 = diff_pattern(wires[3:6])
        diff_5_str = "".join([x[0] for x in diff_5])
     
        segments[0] = [c for c in wires[1] if c not in wires[0]][0] # Top
        segments[2] = [c[0] for c in diff_6 if c[0] in wires[0]][0]
        segments[3] = [c for c in diff_6_str if c not in diff_5_str][0]
        segments[4] = [c for c in diff_6_str if c in diff_5_str and c != segments[2]][0]
        segments[5] = [c for c in wires[0] if c != segments[2]][0]
        segments[1] = [c for c in wires[2] if c not in "".join(segments)][0]
        segments[6] = [c for c in string.ascii_lowercase[:7] if c not in "".join(segments)][0]

        segments = "".join(segments)
        # print(f"Final: {segments}")
        result = ''
        for num in output.split():
            result += str(idx_dict.index(sorted([segments.index(x) for x in num])))
        mega_sum += int(result)
        # print(f"Num {output} -> {result}")
    print("(2) What do you get if you add up all of the output values?")
    print(f"Answer: {mega_sum}")


def main():
    with open("input.txt") as file:
        input_list = [x.strip().split(" | ") for x in file.readlines()]
    part_one(input_list)
    part_two(input_list)

main()