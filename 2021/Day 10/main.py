
def part_one(init_vars, open, points):
    sum_error = 0
    for line in init_vars:
        line_tracker = []
        for char in line:
            if char in open:
                line_tracker.append(char)
            else: #closing char
                if abs(char-line_tracker.pop()) > 2:
                    sum_error += points.get(chr(char))
                    break
    print("(1) What is the total syntax error score for those errors?")
    print(f"Answer: {sum_error}")
    pass

def part_one_shorter(init_vars, opening, points):
    sums = 0
    [
        (tracker := [], s_e := 0, _ :=[(tracker:= tracker + [x]) if x in opening and not s_e else (s_e := s_e + points.get(chr(x)), tracker := tracker[:-1]) if not s_e and abs(x-(tracker[-1])) > 2 else (tracker := tracker[:-1]) for x in line], sums:=sums+s_e)
        for line in init_vars
    ]
    print("(1) What is the total syntax error score for those errors?")
    print(f"Answer: {sums}")

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
                    corrupt = True
        if corrupt:
            continue
        sum_auto = 0
        for x in line_tracker[::-1]:
            sum_auto = 5*sum_auto+points.get(chr(x))
        sums_auto.append(sum_auto)
    print("(2) What is the middle score?")
    print(f"Answer: {sorted(sums_auto)[len(sums_auto)//2]}")
    pass


def main():
    with open("test.txt") as file:
        input_list = [[ord(y) for y in x.strip()]for x in file.readlines() ]
    opening = [40, 60, 91, 123]
    points = {")": 3, "]": 57, "}": 1197, ">": 25137,
              "(": 1, "[":  2, "{": 3, "<":4}
    part_one(input_list, opening, points)
    part_two(input_list, opening, points)
    part_one_shorter(input_list, opening, points)
    
main()
