import copy

def remove_paper(data):
    new_data = copy.deepcopy(data)
    summation = 0
    steps = [-1, 0, 1]
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val != '@':
                continue
            forklifts = [
                data[r+y][c+x]
                for y in steps for x in steps
                if r+y >= 0 and r+y < len(data) and c+x >= 0 and c+x < len(row) and not (y == 0 and x == 0)
            ]
            if a := len(list(filter(lambda x: x == '@', forklifts))) < 4:
                summation += 1
                new_data[r][c] = '.'
    return new_data, summation


def part_one(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.read().strip().splitlines():
            data.append(list(line))
        _, summation = remove_paper(data)    
    return summation


def part_two(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.read().strip().splitlines():
            data.append(list(line))
        total_sum = 0
        while True:
            data, summation = remove_paper(data)    
            total_sum += summation
            if summation == 0:
                break
    return total_sum


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
