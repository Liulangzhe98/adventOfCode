def part_one(input_list):
    counter = sum(1 for prev, curr in zip(input_list, input_list[1:]) if curr > prev)
    print("How many measurements are larger than the previous measurement?")
    print(f"Answer: {counter}")

def part_two(input_list):
    counter = sum(1 for prev, curr in zip(input_list, input_list[3:]) if curr > prev)
    print("How many sums are larger than the previous sum?")
    print(f"Answer: {counter}")

def main():
    with open("input.txt") as file:
        input_list = list(map(int, file.readlines()))
    part_one(input_list)
    part_two(input_list)

main()