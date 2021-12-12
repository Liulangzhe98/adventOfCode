import string

def diff_pattern(wires):
    return list(filter(lambda x: x[1] < len(wires), [(x, "".join(wires).count(x)) for x in string.ascii_lowercase[:7]]))


def part_one(init_vars):
    counter = sum([len(x) in [2, 3, 4, 7] for _, b in init_vars for x in b.split()])
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

def part_two_one_liner(init_vars):
    idx_dict = [[0, 1, 2, 4, 5, 6],[2, 5],[0, 2, 3, 4, 6],[0, 2, 3, 5, 6],[1, 2, 3, 5],[0, 1, 3, 5, 6],[0, 1, 3, 4, 5, 6],[0, 2, 5],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 5, 6]]
    mega_sum = 0
    for wires, output in init_vars:
        sets = sorted([set([x for x in w]) for w in wires.split()], key=lambda x:len(x))
        full_segment = set([x for x in string.ascii_lowercase[:7]])
        mid_set = set.intersection(*sets[3:6])
        other_set = set.intersection(*sets[6:9])
        segments = "".join([sets[1].difference(sets[0]).pop(), full_segment.difference(mid_set, sets[0]).intersection(other_set).pop(), sets[1].intersection(full_segment.difference(other_set)).pop(), mid_set.intersection(full_segment.difference(other_set)).pop(), full_segment.difference(mid_set, sets[2]).pop(), sets[0].difference(full_segment.difference(other_set)).pop(), full_segment.intersection(mid_set).difference(sets[1], full_segment.difference(other_set)).pop()])
        mega_sum += int("".join([ str(idx_dict.index(sorted([segments.index(x) for x in num]))) for num in output.split()]))
    print("(2) What do you get if you add up all of the output values?")
    print(f"Answer: {mega_sum}")

def main():
    with open("test.txt") as file:
        input_list = [x.strip().split(" | ") for x in file.readlines()]
    part_one(input_list)
    part_two(input_list)
    part_two_one_liner(input_list)

main()