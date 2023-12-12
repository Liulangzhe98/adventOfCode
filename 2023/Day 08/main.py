from collections import namedtuple, defaultdict
import re
from math import lcm

node = namedtuple("Node" , ["L", "R"])


def part_one(file_path):
    with open(file_path, 'r') as file:
        nodes = {}
        moves, pairs = file.read().strip().split("\n\n")
        for p in pairs.splitlines():
            label, l , r = re.findall("\w{3}", p)
            nodes[label] = node(l, r)
        current = "AAA"
        steps = 0
        while current != "ZZZ":
            next_node = nodes[current]
            move = moves[steps%len(moves)]
            current = next_node[move == "R"]
            steps += 1
    return steps


def part_two(file_path):
    with open(file_path, 'r') as file:
        nodes = {}
        moves, pairs = file.read().strip().split("\n\n")
        for p in pairs.splitlines():
            label, l , r = re.findall("\w{3}", p)
            nodes[label] = node(l, r)
        curr_nodes = list(filter(lambda x: x.endswith("A"), nodes.keys()))
        ending = [x.endswith("Z") for x in curr_nodes]
        paths = []
        for current in curr_nodes:
            steps = 0
            while current[2] != "Z":
                next_node = nodes[current]
                move = moves[steps%len(moves)]
                current = next_node[move == "R"]
                steps +=1
            paths.append(steps)
    return lcm(*paths)


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test_2.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
