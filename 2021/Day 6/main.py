import re

def part_one(input_list, my_dict):
    MAX_DEPTH = 80
    rec_dict = {}
    for x in range(1, 8):
        rec_dict[x-1] = recursion(x, MAX_DEPTH,my_dict)
    x = [my_dict.get(y+1) for y in input_list]
    print("(1) How many lanternfish would there be after 80 days?")
    print(f"Answer: {sum(x)}")


def part_two(input_list, my_dict):
    MAX_DEPTH = 256
    rec_dict = {}
    for x in range(1, 8):
        rec_dict[x-1] = recursion(x, MAX_DEPTH,my_dict)
    x = [my_dict.get(y+1) for y in input_list]
    print("(2) How many lanternfish would there be after 256 days?")
    print(f"Answer: {sum(x)}")

    
def init():
    with open("input.txt") as file:
        input_list = [int(x) for x in file.readline().split(",")]
    return input_list

def recursion(depth, MAX, my_dict):
    if my_dict.get(depth):
        return my_dict.get(depth)

    if depth > MAX:
        return 1
    output = recursion(depth+7, MAX,my_dict)+recursion(depth+9, MAX,my_dict)
    my_dict[depth] = output
    return output


def main():
    init_vars = init()
    part_one(sorted(init_vars), {})
    part_two(sorted(init_vars), {}) 
 

main()