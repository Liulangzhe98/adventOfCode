def solver(input_list, my_dict, MAX_DEPTH=80):
    [recursion(x, MAX_DEPTH,my_dict) for x in range(1, 8)]
    return sum([my_dict.get(y+1) for y in input_list])
    
def recursion(depth, MAX, my_dict):
    if my_dict.get(depth):
        return my_dict.get(depth)
    if depth > MAX:
        return 1
    output = recursion(depth+7, MAX,my_dict)+recursion(depth+9, MAX,my_dict)
    my_dict[depth] = output
    return output

def main():
    init_vars = [int(x) for x in open("input.txt").readline().split(",")]
    print("(1) How many lanternfish would there be after 80 days?")
    print(f"Answer: {solver(init_vars, {}, 80)}")
    print("(2) How many lanternfish would there be after 256 days?")
    print(f"Answer: {solver(init_vars, {}, 256)}")

main()