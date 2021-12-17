import re
import math

def part_one(x1, x2, y1, y2):
    x_possible = [ (i, [max(0, i-j) for j in range(10)]) for i in range(10)]
    for i in range(1, x2):
        x_possible = (i, sum(range(i+1)))
        if x_possible[1] >= x1:
            break
    least_steps = x_possible[0]

    #determine y
    max_coord = (0,0)
    for y in range(least_steps, 100):
        step = least_steps
        while True:
            my_sum = 0
            tracker = []
            for i in range(y, y-step, -1):
                my_sum += i
                tracker.append(my_sum)
            if my_sum < y1:
                break
            if my_sum <= y2:
                max_coord = max(max_coord, (y, max(tracker)), key=lambda x: x[1])
                break
            step += 1
    print("(1) What is the highest y position it reaches on this trajectory?")
    print(f"Answer: {max_coord[1]}")

def part_one_math(lowest):
    print("(1) What is the highest y position it reaches on this trajectory?")
    print(f"Answer: {lowest*(lowest-1)//2}")

def part_two(x1, x2, y1, y2):
    steps_possible = []
    for ele in range(y1, -y1):
        b = []
        i = ele
        my_sum = 0
        while True:
            b.append(my_sum)
            my_sum += i
            i -= 1
            if my_sum <= y1:
                break
        steps_possible.append((ele, b))
    total = 0
    for idx in range(1, x2+1):
        for start_y in steps_possible:
            coord = (0,0)
            dx, dy = idx, start_y[0]
            while True: # do step
                coord = (coord[0]+dx, coord[1]+dy)
                dx = max(0, dx-1)
                dy -= 1
                if x1 <= coord[0] <= x2 and y1 <= coord[1] <= y2:
                    total += 1
                    break
                if coord[1] <= y1 or coord[0] > x2:
                    break
    print(total)
    print("(2) How many distinct initial velocity values cause the probe to be within the target area after any step?")
    print(f"Answer: {total}")


def main():
    with open("input.txt") as file:
        x1, x2, y1, y2 = map(int, re.findall("(-?\d+)", file.readline()))
    part_one(x1, x2, y1, y2)
    part_two(x1, x2, y1, y2)
    part_one_math(abs(y1))


main()
