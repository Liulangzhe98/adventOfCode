import z3
from z3 import *
import math
from itertools import product


def part_one(file_path):
    with open(file_path, "r") as file:
        total = 0
        for line in file.read().strip().splitlines():
            splits = line.split()
            indicator, buttons, joltage = splits[0], splits[1:-1], splits[-1]
            indicator = tuple(int(x == "#") for x in indicator[1:-1])
            a = bfs([0] * len(indicator), buttons, indicator)
            total += a
    return total


def bfs(start, buttons, indicator):
    current = [tuple(start)]
    visited = set()
    steps = 1
    while True:
        new = []
        for lights in current:
            visited.add(lights)
            for button in buttons:
                new_lights = tuple(
                    (x - 1) * -1 if str(idx) in button else x
                    for idx, x in enumerate(lights)
                )
                if new_lights == indicator:
                    return steps
                if new_lights not in visited:
                    new.append(new_lights)
        steps += 1
        current = new


def part_two(file_path):
    with open(file_path, "r") as file:
        total = 0
        for line in file.read().strip().splitlines():
            splits = line.split()
            minimal_steps = math.inf
            indicator, buttons, joltage = splits[0], splits[1:-1], splits[-1]
            buttons = [
                eval(x[:-1] + ",)") if "," not in x else eval(x) for x in buttons
            ]
            joltage = [int(x) for x in joltage[1:-1].split(",")]
            total += solve_part2_z3(joltage, buttons)

    return total


def solve_part2_z3(target, buttons):
    n_counters = len(target)
    n_buttons = len(buttons)

    # Declare integer variables (one per button)
    presses = [Int(f"p{i}") for i in range(n_buttons)]

    opt = Optimize()

    # Constraint: Can't press a button negative times
    for p in presses:
        opt.add(p >= 0)

    # Constraint: Each counter must reach its target
    for counter_idx in range(n_counters):
        total = sum(
            presses[btn_idx]
            for btn_idx, btn in enumerate(buttons)
            if counter_idx in btn
        )
        opt.add(total == target[counter_idx])

    # Minimize total presses
    opt.minimize(Sum(presses))

    if opt.check() == sat:
        m = opt.model()
        return sum(m[p].as_long() for p in presses)
    return None


def timed_print(text, func, file):
    import time

    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end - start) * 1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")


if __name__ == "__main__":
    main()
