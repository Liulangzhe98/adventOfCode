import re
import math 
 
 
# function for finding roots
def equationroots( a, b, c): 
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
     
    if dis > 0: 
        return (-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a) 
    elif dis == 0: 
        return -b / (2 * a) 
    else:
        return (- b / (2 * a), + i, sqrt_val), (- b / (2 * a), - i, sqrt_val) 



def part_one(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
        time = [int(x) for x in re.findall("\d+", lines[0])]
        distance = [int(x) for x in re.findall("\d+", lines[1])]
        solution = 1
        for t, d in zip(time, distance):
            score = equationroots(-1, t, -d-0.01)
            number = (math.floor(score[1])-math.ceil(score[0]))
            solution *= (number+1) # Offset due to subtraction != length of range
    return solution



def part_two(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
        time = [int(x) for x in re.findall("\d+", lines[0].replace(" ", ""))]
        distance = [int(x) for x in re.findall("\d+", lines[1].replace(" ", ""))]
        solution = 1
        for t, d in zip(time, distance):
            score = equationroots(-1, t, -d-0.01)
            number = (math.floor(score[1])-math.ceil(score[0]))
            solution *= (number+1) # Offset due to subtraction != length of range
    return solution


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
