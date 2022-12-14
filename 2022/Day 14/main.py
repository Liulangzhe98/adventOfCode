def get_range(a, b):
    a, b = (int(a), int(b))
    if a < b:
        return list(range(a, b+1))
    return list(range(b, a+1))


def int_check(a, b):
    # Same as the sign check of day 9 but now with b being variable instead of 0
    return (a > b) - (a<b)


def part_one(file_path):
    walls = []
    with open(file_path, 'r') as file:
        for e, path in enumerate(file.read().splitlines()):
            steps = list(map(lambda s: list(map(int, s.split(','))), path.split(' -> ')))
            for (ax, ay), (bx, by) in zip(steps, steps[1:]):
                for x in range(min(ax, bx), max(ax, bx)+1):
                    for y in range(min(ay, by), max(ay, by)+1):
                        walls.append((x, y))
    walls = list(set(walls))
    lowest = max(walls, key=lambda x: x[1])[1]

    resting = 0
    moves = [(0, 1), (-1, 1), (1, 1)]
    endless = False
    path = [(500, 0)] 
    while not endless:
        x, y = path.pop()
        rest = False
        while not rest:
            if y > lowest:
                endless = True
                break
            path.append((x, y))
            if (new := (x, y+1)) not in walls:
                x, y, = new
            elif (new := (x-1, y+1)) not in walls:
                x, y, = new
            elif (new := (x+1, y+1)) not in walls:
                x, y, = new
            else:
                rest = True
                resting += 1
                path.pop()
        walls.append((x, y))   
    return resting


def part_two(file_path):
    walls = []
    with open(file_path, 'r') as file:
        for e, path in enumerate(file.read().splitlines()):
            steps = list(map(lambda s: list(map(int, s.split(','))), path.split(' -> ')))
            for (ax, ay), (bx, by) in zip(steps, steps[1:]):
                for x in range(min(ax, bx), max(ax, bx)+1):
                    for y in range(min(ay, by), max(ay, by)+1):
                        walls.append((x, y))
    walls = list(set(walls))
    lowest = max(walls, key=lambda x: x[1])[1]+2

    next_post = [(500, 0)]
    moves = [(0, 1), (-1, 1), (1, 1)]
    visited = 1
    for i in range(lowest-1):
        tracker = set([(cx+m[0], cy+m[1]) 
            for (cx, cy) in next_post for m in moves])
        next_post = list(tracker.difference(walls))
        visited += len(next_post)
    return visited


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    
    
if __name__ == "__main__":
    main()
