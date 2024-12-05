from collections import defaultdict


def part_one(file_path):
    with open(file_path, 'r') as file:
        array = []
        for line in file.read().strip().splitlines():
            array.append([x for x in line])
        max_width = len(array[0])
        max_height = len(array)
        counts = 0
        for e, row in enumerate(array):
            for c, _ in enumerate(row):
                # left to right
                if c <= (max_width-4):
                    counts += "".join(row[c:c+4]) == "XMAS"

                # right to left
                if c >= 3:
                    counts += "".join(row[c-3:c+1]) == "SAMX"
                # up to down
                if e <= (max_height-4):
                    xmas = "".join([array[e+i][c] for i in range(4)])
                    counts += (xmas == "XMAS")
                # down to up
                if e >= 3:
                    xmas = "".join([array[e-i][c] for i in range(4)])
                    counts += (xmas == "XMAS")

                # diagonal left to right
                diag_1 = []
                diag_2 = []
                diag_3 = []
                diag_4 = []
                for i in range(4):
                    if not ((not 0 <= e + i < max_height) or (not 0 <= c + i < max_width)):
                        diag_1.append(array[e+i][c+i])
                    if not ((not 0 <= e + i < max_height) or (not 0 <= c - i < max_width)):
                        diag_2.append(array[e+i][c-i])
                    if not ((not 0 <= e - i < max_height) or (not 0 <= c + i < max_width)):
                        diag_3.append(array[e-i][c+i])
                    if not ((not 0 <= e - i < max_height) or (not 0 <= c - i < max_width)):
                        diag_4.append(array[e-i][c-i])

                for d in [diag_1, diag_2, diag_3, diag_4]:
                    xmas = "".join(filter(lambda x: x, d))
                    counts += xmas == "XMAS"

    return counts


def part_two(file_path):
    with open(file_path, 'r') as file:
        array = []
        for line in file.read().strip().splitlines():
            array.append([x for x in line])
        count = 0
        for y in range(len(array)-2):
            for x in range(len(array[0])-2):
                count += (
                    array[y][x] + array[y+1][x+1] + array[y+2][x+2] in ("MAS", "SAM")
                    and array[y][x+2] + array[y+1][x+1] + array[y+2][x] in ("MAS", "SAM")
                )
    return count


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
