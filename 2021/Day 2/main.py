def sign(x):
    return -1 if x < 0 else 1

def part_one(input_list):
    pos = depth = 0
    for d, v in input_list:
        if d == "up":
            depth -= v
        elif d == "down":
            depth += v
        else:
            pos += v
    print("(1) What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")

def part_one_one_liner(input_list):
    pos = depth = 0
    [(pos := pos + v) if d.startswith("f") else (0, depth := depth - v*sign(ord(d[0])-ord('e'))) for d, v in input_list]

    print("(1) What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")


def part_two(input_list):
    pos = depth = aim = 0
    for d, v in input_list:
        if d == "up":
            aim -= v
        elif d == "down":
            aim += v
        else:
            pos += v
            depth += aim*v
    print("(2) What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")

def part_two_one_liner(input_list):
    pos = depth = aim = 0
    [(pos := pos + v, depth:= depth+aim*v) if d.startswith("f") else (aim:= aim + (v*-1*sign(ord(d[0])-ord('e')))) for d, v in input_list]
    print("(2) What do you get if you multiply your final horizontal position by your final depth?")
    print(f"Answer: pos: {pos} depth: {depth} -> {pos*depth}")
    

def main():
    with open("input.txt") as file:
        input_list = [x.strip().split(" ") for x in file.readlines()]
        input_list = [(d, int(v)) for d, v in input_list]
    part_one(input_list)
    part_two(input_list)
    print(" === one liners === ")
    part_one_one_liner(input_list)
    part_two_one_liner(input_list)

main()