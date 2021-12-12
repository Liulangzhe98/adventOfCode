
def part_one(init_vars):
    last_line = len(init_vars)
    last_col = len(init_vars[0])
    counter = 0
    for r, row in enumerate(init_vars):
        for c, col in enumerate(row):
            smallest = [ 
                True if c%last_col == last_col-1 else col < init_vars[r][c+1], # right
                True if r%last_line == last_line-1 else col < init_vars[r+1][c], # bottom
                True if c == 0 else col < init_vars[r][c-1], # left
                True if r == 0 else col < init_vars[r-1][c], # top
            ]
            counter += (col+1)*all(smallest)
    print("(1) What is the sum of the risk levels of all low points on your heightmap?")
    print(f"Answer: {counter}")

def part_one_one_liner(init_vars):
    counter = [ 
        all([ 
                True if c == (len(init_vars[0]) -1) else col < init_vars[r][c+1], # right
                True if r == (len(init_vars)    -1) else col < init_vars[r+1][c], # bottom
                True if c == 0 else col < init_vars[r][c-1], # left
                True if r == 0 else col < init_vars[r-1][c], # top
            ])*(col+1)
        for r, row in enumerate(init_vars) for c, col in enumerate(row)
    ]
    print("(1) What is the sum of the risk levels of all low points on your heightmap?")
    print(f"Answer: {sum(counter)}")

def part_two(init_vars):
    last_line = len(init_vars)
    last_col = len(init_vars[0])
    visited = [[False for _ in range(len(init_vars[0]))] for _ in range(len(init_vars))]
    basins = []
    for r in range(last_line):
        for c in range(last_col):
            if init_vars[r][c] != 9 and not visited[r][c]:
                to_visit = [(c,r)] # (x, y)
                visited[r][c] = True
                basin = 0
                while to_visit != []:
                    x, y  = to_visit.pop(0)
                    basin += 1
                    conditions = [ 
                        (x != last_col-1  and not visited[y][x+1] and init_vars[y][x+1] != 9, (x+1, y)), #right
                        (y != last_line-1 and not visited[y+1][x] and init_vars[y+1][x] != 9, (x, y+1)), #bottom
                        (x != 0 and not visited[y][x-1] and init_vars[y][x-1] != 9, (x-1, y)), #left
                        (y != 0 and not visited[y-1][x] and init_vars[y-1][x] != 9, (x, y-1)), #top
                    ]
                    for c, m in conditions:
                        if c:
                            to_visit.append(m)
                            visited[m[1]][m[0]] = True
                basins.append(basin)      

    r =1
    [r := r*x for x in sorted(basins, reverse=True)[:3]]
    print("(2) What do you get if you multiply together the sizes of the three largest basins?")
    print(f"Answer: {r}")

def set_true(v, x, y):
    v[y][x][1] = 9
    return True

def part_two_shorter(init_vars):
    x_max, y_max = len(init_vars[0]), len(init_vars)
    v = [[[x, 0] for x in y] for y in init_vars]
    basins = (0, 0, 0)
    for r in range(y_max):
        for c in range(x_max):
            if 9 not in v[r][c]:
                to_visit = [(c,r)] # (x, y)
                v[r][c][1] = True
                basin = -1
                while to_visit != []:
                    x, y  = to_visit.pop(0)
                    basin += 1
                    conditions = [ 
                        (x != x_max-1 and 9 not in v[y][x+1], (x+1, y)), #right
                        (y != y_max-1 and 9 not in v[y+1][x], (x, y+1)), #bottom
                        (x != 0       and 9 not in v[y][x-1], (x-1, y)), #left
                        (y != 0       and 9 not in v[y-1][x], (x, y-1)), #top
                    ]
                    [(_:= to_visit.append(m), _:= set_true(v, *m)) for c, m in conditions if c]
                basins = (basins[1], basins[2], basin) if basin >= basins[2] else (basins[1], basin, basins[2]) if basin >= basins[1] else (basin, basins[1], basins[2]) if basin >= basins[0] else basins
    print("(2) What do you get if you multiply together the sizes of the three largest basins?")
    print(f"Answer: {basins[0]*basins[1]*basins[2]}")


def main():
    with open("input.txt") as file:
        input_list = [[int(y) for y in x.strip()]for x in file.readlines() ]
    part_one(input_list)
    part_two(input_list)
    part_one_one_liner(input_list)
    part_two_shorter(input_list)
    
main()