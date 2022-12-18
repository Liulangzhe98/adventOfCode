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

def print_red(text):
    print(f"{bcolors.FAIL}{text}{bcolors.ENDC}")

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
        # print(f"[{y}, {start_width}] = {rock[i]} vs {''.join(chamber[y])[start_width:]}")
        for (a1, b1) in zip(rock[i], ''.join(chamber[y])[start_width:]):
            # print(f"[{e}] = {a1} vs {b1}")
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
    # print("Checking out: ", rock)  
    # print(start_height, start_width)
    for e, (a, b) in enumerate(zip(rock[::-1], chamber[start_height:]), start_height):
        b = "".join(b)
        for (a1, b1) in zip(a, b[start_width:]):
            # print(f"[{e}] = {a1} vs {b1}")
            if a1 == b1 and a1 == '#':
                return False

    return True

def check_left(start_height, start_width, rock, chamber):
    if start_width <= 0:
        return False
    start_width -= 1
    # print("Checking out: ", rock)  
    # print(start_height, start_width)
    for e, (a, b) in enumerate(zip(rock[::-1], chamber[start_height:]), start_height):
        b = "".join(b)
        for (a1, b1) in zip(a, b[start_width:]):
            # print(f"[{e}] = {a1} vs {b1}")
            if a1 == b1 and a1 == '#':
                return False

    return True



def solve(jet, count):
    chamber = [["." for _ in range(7)] for _ in range(15)]
    highest = 0
    prev = None

    len_gust = len(jet)
    
    find_pattern = {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : []
    }

    find_pattern2 = {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : []
    }

    gust = 0
    i = 0

    height_offset = 0
    found_skip = False

    while i < count:
        # print(i)
        # if i % (count//20) == 0 and i > 0:
            # print(f"Done: {i/count:.2%}")
        
        rock = rocks[i%len(rocks)]

        find_pattern[i%len(rocks)].append((gust%len_gust, i, highest))
        find_pattern2[i%len(rocks)].append(gust%len_gust)

        if not found_skip and i%len(rocks) == 0 and (gust%len_gust in find_pattern2[0]):
            b = [str(x[0]) for x in find_pattern[0]]
            result = int(get_pattern(b)[0])
            if result > 0 :
                blub = list(filter(lambda s: s[0] == result, find_pattern[0]))
                print(blub)
                height_gain = blub[1][2]-blub[0][2]
                rocks_cycle = blub[1][1]-blub[0][1]
                skips = (count-i)//rocks_cycle
                skips = max(0, skips-10)
                print(f"can skip cycles: {skips} ==> {i+skips*rocks_cycle} | {skips*height_gain}")
                i += skips*rocks_cycle
                height_offset = skips*height_gain
                found_skip = True

                # return None

        start_width = 2
        start_height = highest + 3

        height = start_height
        move_down = False
        floor = False
        steps = []
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
                        steps.append(pushed)
                    else:
                        steps.append(" ")
                else:
                    if check_left(start_height, start_width, rock, chamber):
                        start_width -= 1
                        steps.append(pushed)
                    else:
                        steps.append(" ")
                    pass
                jet += pushed
        new_highest = placement(start_height, start_width, rock, chamber)
        prev = highest + 3
        highest = max(new_highest, highest)
        for _ in range(highest+8-len(chamber)):
            chamber.append(["." for _ in range(7)] )
        i += 1

    # for k, v in find_pattern.items():
    #     b = [str(x[0]) for x in v]
    #     print(k, v, get_pattern(b)[0])
    #     break

    print(highest, highest+height_offset)
    return highest+height_offset

def part_one(file_path):
    with open(file_path, 'r') as file:
        jet = [x for x in file.read().splitlines()[0]]
        return solve(jet, count=2022)


def get_pattern(seq):
    seq2 = seq
    outs = {}
    l = 0
    r = 0
    c = None

    for end in range(len(seq2)+1):
      for start in range(end):
          word = chr(1).join(seq2[start:end])
          if not word in outs:
              outs[word] = 1
          else:
              outs[word] += 1
    for item in outs:
        if outs[item] > r or (len(item) > l and outs[item] > 1):
            l = len(item)
            r = outs[item]
            c = item
    return c.split(chr(1))


def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def part_two(file_path):
    with open(file_path, 'r') as file:
        jet = [x for x in file.read().splitlines()[0]]
        return solve(jet, count=1000000000000)

def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")

rocks = [
    ["####"], 
    [".#.","###",".#."], 
    ["..#","..#","###"], 
    ["#","#","#","#"] ,
    ["##","##"]
]




# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

def main():
    timed_print("Solution 1T", part_one, "test.txt") # 3068 with 2022 rocks
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt") # 5500 -> 8379 ??
    timed_print("Solution 2 ", part_two, "input.txt")   # 1531594202866 too high
                                                        # 1531594202837
     
if __name__ == "__main__":
    main()
