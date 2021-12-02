def part_one(input_list):
    pos = depth = 0
    for d, v in input_list:
        if d == "up":
            depth -= int(v)
        elif d == "down":
            depth += int(v)
        else:
            pos += int(v)
    print("What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")


def part_two(input_list):
    pos = depth = aim = 0
    for d, v in input_list:
        if d == "up":
            aim -= int(v)
        elif d == "down":
            aim += int(v)
        else:
            pos += int(v)
            depth += aim*int(v)
    print("What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")

def main():
    with open("input.txt") as file:
        input_list = [x.strip().split(" ") for x in file.readlines()]
    part_one(input_list)
    part_two(input_list)

main()