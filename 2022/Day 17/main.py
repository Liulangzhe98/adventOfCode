class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def placement(start_height, start_width, rock, chamber):
    for y, line in enumerate(rock[::-1], start_height):
        for x, cell in enumerate(line, start_width):
            if cell == "#":
                chamber[y][x] = cell
    return y+1


def check_down(start_height, start_width, rock, chamber):
    if start_height == -1:
        return False
    for i in range(len(rock)):
        y = start_height+len(rock)-i-1
        for (a1, b1) in zip(rock[i], ''.join(chamber[y])[start_width:]):
            if a1 == b1 and a1 == '#':
                return False
    size = len(rock[-1])
    check = "".join(chamber[start_height][start_width:])
    for a, b, in zip(rock[-1], check):
        if a == b and a == '#':
            return False
    return True
    

def check_right(start_height, start_width, rock, chamber):
    if start_width + len(rock[0]) >= 7:
        return False
    start_width += 1
    for e, (a, b) in enumerate(zip(rock[::-1], chamber[start_height:]), start_height):
        b = "".join(b)
        for (a1, b1) in zip(a, b[start_width:]):
            if a1 == b1 and a1 == '#':
                return False
    return True


def check_left(start_height, start_width, rock, chamber):
    if start_width <= 0:
        return False
    start_width -= 1
    for e, (a, b) in enumerate(zip(rock[::-1], chamber[start_height:]), start_height):
        b = "".join(b)
        for (a1, b1) in zip(a, b[start_width:]):
            if a1 == b1 and a1 == '#':
                return False
    return True


def solve(jet, count):
    chamber = [["." for _ in range(7)] for _ in range(15)]
    highest = 0
    prev = None

    len_gust = len(jet)
    gust = 0
    i = 0

    tracked = {}

    while i < count:  
        rock = rocks[i%len(rocks)]

        key = (i%len(rocks), gust%len_gust)
        if key in tracked:
            prev, elevation = tracked[key]
            period = i - prev
            if i % period == count % period :
                height_gain = highest-elevation
                skips = (count-i)//period
                return highest + skips*height_gain
        else:
            tracked[key] = (i, highest)

        start_width = 2
        start_height = highest + 3

        height = start_height
        move_down = False
        floor = False
        while not floor:
            if move_down:
                move_down = False
                start_height -= 1
                if not check_down(start_height, start_width, rock, chamber):
                    start_height = max(0, start_height+1)
                    floor = True    
            else:
                pushed = jet.pop(0)
                gust += 1 
                move_down = True
                if pushed == ">":
                    # move right
                    if check_right(start_height, start_width, rock, chamber):
                        start_width += 1
                else:
                    if check_left(start_height, start_width, rock, chamber):
                        start_width -= 1
                jet += pushed

        new_highest = placement(start_height, start_width, rock, chamber)
        prev = highest + 3
        highest = max(new_highest, highest)

        for _ in range(highest+8-len(chamber)):
            chamber.append(["." for _ in range(7)] )
        i += 1
    return highest


def part_one(file_path):
    with open(file_path, 'r') as file:
        jet = [x for x in file.read().splitlines()[0].strip()]
        return solve(jet, count=5500)


def part_two(file_path):
    with open(file_path, 'r') as file:
        jet = [x for x in file.read().splitlines()[0].strip()]
        return solve(jet, count=1000000000000)


rocks = [
    ["####"], 
    [".#.","###",".#."], 
    ["..#","..#","###"], 
    ["#","#","#","#"] ,
    ["##","##"]
]


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt") # 3068 with 2022 rocks, 5500 -> 8334
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt") # 5500 -> 8379 
    timed_print("Solution 2 ", part_two, "input.txt")   # 1531594202749 too high


if __name__ == "__main__":
    main()
