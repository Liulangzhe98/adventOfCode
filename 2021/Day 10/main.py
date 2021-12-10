
def part_one(init_vars, open, points):
    sum_error = 0
    for line in init_vars:
        line_tracker = []
        corrupt = False
        for char in line:
            if char in open:
                line_tracker.append(char)
            else: #closing char
                if abs(char-line_tracker.pop()) > 2:
                    # print(f"corrupt => {line}")
                    # print(f"Found: {chr(char)} => {points.get(chr(char))}")
                    # print("===================")
                    corrupt = True
                    sum_error += points.get(chr(char))
                    continue
        if corrupt:
            continue
    print("(1) What is the total syntax error score for those errors?")
    print(f"Answer: {sum_error}")
    pass


def part_two(init_vars, open, points):
    sums_auto = []
    for line in init_vars:
        line_tracker = []
        corrupt = False
        for char in line:
            if char in open:
                line_tracker.append(char)
            else: #closing char
                if abs(char-line_tracker.pop()) > 2:
                    print(f"corrupt => {line}")
                    print(f"Found: {chr(char)} => {points.get(chr(char))}")
                    print("===================")
                    corrupt = True
                    continue
        if corrupt:
            continue
        print(f"Line: {line} || {[chr(x) for x in line_tracker]}")
        sum_auto = 0
        for x in line_tracker[::-1]:
            sum_auto = 5*sum_auto+points.get(chr(x))
            print(f"{chr(x)} -> {points.get(chr(x))}")
        sums_auto.append(sum_auto)
    print("(1) What is the middle score?")
    print(f"Answer: {sorted(sums_auto)[len(sums_auto)//2]}")
    pass


def main():
    with open("input.txt") as file:
        input_list = [[ord(y) for y in x.strip()]for x in file.readlines() ]
    opening = [40, 60, 91, 123]
    closing = [41, 62, 93, 125]
    points = {")": 3, "]": 57, "}": 1197, ">": 25137,
              "(": 1, "[":  2, "{": 3, "<":4}
    part_one(input_list, opening, points)
    part_two(input_list, opening, points)
    
main()
