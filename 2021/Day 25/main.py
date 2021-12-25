import copy

def do_step_east(matrix, east, WIDTH=10):
    next_step = copy.deepcopy(matrix)
    moved = False
    new_east = []
    for x in east:
        if not matrix[x[0]][(x[1]+1)%WIDTH]:
            next_step[x[0]][(x[1]+1)%WIDTH] = 1
            next_step[x[0]][x[1]] = 0
            new_east.append((x[0], (x[1]+1)%WIDTH))
            moved = True
        else:
            next_step[x[0]][x[1]] = 1
            new_east.append(x)
    return next_step, new_east.copy(), moved

def do_step_south(matrix, south, HEIGHT=8):
    next_step = copy.deepcopy(matrix)
    moved = False
    new_south = []
    for x in sorted(south, key=lambda x: x[0]):
        if not matrix[(x[0]+1)%HEIGHT][x[1]]:
            next_step[(x[0]+1)%HEIGHT][x[1]] = 2
            next_step[x[0]][x[1]] = 0
            new_south.append(((x[0]+1)%HEIGHT, x[1]))
            moved = True
        else:
            next_step[x[0]][x[1]] = 2
            new_south.append(x)
    return next_step, new_south.copy(), moved

def main():
    with open("input.txt") as file:
        input_blob = file.read()

    east_herd = []
    south_herd = []
    matrix = []

    for r, line in enumerate(input_blob.split("\n")):
        row_m = []
        for c, char in enumerate(line):
            
            if char in ">v":
                if char == 'v':
                    south_herd.append((r, c))
                    row_m.append(2)
                else:
                    east_herd.append((r, c))
                    row_m.append(1)
            else:
                row_m.append(0)
        matrix.append(row_m)
    MAX_WIDTH = len(row_m)
    MAX_HEIGHT = len(matrix)
    moved = True
    counter = 0
    while moved:
        counter += 1
        matrix, east_herd, moved_e = do_step_east(matrix, east_herd, MAX_WIDTH)
        matrix, south_herd, moved_s = do_step_south(matrix, south_herd, MAX_HEIGHT)
        print(f"At {counter}", end="\r")

        # print_as_matrix(matrix)
        moved = moved_e or moved_s

    print("(1) What is the first step on which no sea cucumbers move?")
    print(f"Answer: {counter}")

   
    

main()
