def print_as_matrix(matrix):
    print("[")
    for i in range(len(matrix)):
        print(f"  {matrix[i]}")
    print("]")

def get_adjacent_cells(x, y, neighbours, xmax=10, ymax=10):
     for dx, dy in neighbours:
          if 0 <= (x + dx) < xmax and 0 <= y + dy < ymax: #boundaries check
#yielding is usually faster than constructing a list and returning it if you're just using it once
              yield (x + dx, y + dy)

def part_one(init_vars, neighbours):
    flashed = 0
    for step in range(1, 101):
        init_vars = [[y+1 for y in x] for x in init_vars]
        ignore_octo = []
        flashy = [(r,c) for r, row in enumerate(init_vars) for c, col in enumerate(row) if col > 9 and (r,c) not in ignore_octo]
        while flashy != []:
            for octo in flashy:
                for (o_x, o_y) in get_adjacent_cells(octo[1], octo[0], neighbours):
                    init_vars[o_y][o_x] += 1
                ignore_octo.append(octo)
            flashy = [(r,c) for r, row in enumerate(init_vars) for c, col in enumerate(row) if col > 9 and (r,c) not in ignore_octo]
        for (y, x) in ignore_octo:
            init_vars[y][x] = 0
        flashed += len(ignore_octo)
    print("(1) How many total flashes are there after 100 steps?")
    print(f"Answer: {flashed}")



def part_two(init_vars, neighbours):
    flashed = 0
    step = 1
    while True:
        init_vars = [[y+1 for y in x] for x in init_vars]
        ignore_octo = []
        flashy = [(r,c) for r, row in enumerate(init_vars) for c, col in enumerate(row) if col > 9 and (r,c) not in ignore_octo]
        while flashy != []:
            for octo in flashy:
                for (o_x, o_y) in get_adjacent_cells(octo[1], octo[0], neighbours):
                    init_vars[o_y][o_x] += 1
                ignore_octo.append(octo)
            flashy = [(r,c) for r, row in enumerate(init_vars) for c, col in enumerate(row) if col > 9 and (r,c) not in ignore_octo]
        for (y, x) in ignore_octo:
            init_vars[y][x] = 0
        flashed += len(ignore_octo)
        if len(ignore_octo) == 100:
            break
        step += 1
    print("(2) What is the first step during which all octopuses flash?")
    print(f"Answer: {step}")


def main():
    with open("input.txt") as file:
        input_list = [[int(y) for y in x.strip()] for x in file.readlines()]
    neighbours = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    part_one(input_list, neighbours)
    part_two(input_list, neighbours)
    
main()
