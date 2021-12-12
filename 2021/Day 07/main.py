import statistics
from functools import reduce


def part_one(init_vars):
    print("(1) How much fuel must they spend to align to that position?")
    print(f"Answer: {sum([abs(x-int(statistics.median(init_vars))) for x in init_vars])}")

def part_two(init_vars):
    print("(2) How much fuel must they spend to align to that position?")
    print(f"Answer: {min([sum([(abs(v-x)*(abs(v-x)+1)//2) for x in init_vars]) for v in [int(sum(init_vars)/len(init_vars)), int(sum(init_vars)/len(init_vars))+1]])}")

def main():
    init_vars = sorted([int(x) for x in open("input.txt").readline().split(",")])
    part_one(init_vars)
    part_two(init_vars)

main()