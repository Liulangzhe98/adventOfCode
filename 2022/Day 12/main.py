import math

def do_move(coord, move):
    x = coord[0]+move[0]
    y = coord[1]+move[1]
    if x < 0 or y < 0:
        return coord
    return (x, y)

def BFS(matrix, start, end):
    Q = [(0, start)]
    visited = set()
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while Q != []:
        cost, coord = Q.pop(0)
        if coord == end:
            return cost
        if coord in visited:
            continue
        visited.add(coord)
        cur_val = matrix[coord[0]][coord[1]]
        for move in moves:
            new_coord = do_move(coord, move)
            try:
                val = matrix[new_coord[0]][new_coord[1]]
                if cur_val + 1 >= val:
                    Q.append((cost+1, new_coord))
            except:
                pass
    return math.inf


def part_one(file_path):
    matrix = []
    start_coord = None
    end_coord = None
    with open(file_path, 'r') as file:
        for r, line in enumerate(file.read().splitlines()):
            l = []
            for c, cell in enumerate(line):
                if cell == "S":
                    start_coord = (r, c)
                    cell = 'a'
                if cell == "E":
                    end_coord = (r, c)
                    cell = 'z'
                l.append(ord(cell)-ord('a'))
            matrix.append(l)
    return BFS(matrix, start_coord, end_coord)


def part_two(file_path):
    matrix = []
    start_coord = []
    end_coord = None
    with open(file_path, 'r') as file:
        for r, line in enumerate(file.read().splitlines()):
            l = []
            for c, cell in enumerate(line):
                if cell == "S" or cell == "a":
                    start_coord.append((r, c))
                    cell = 'a'
                if cell == "E":
                    end_coord = (r, c)
                    cell = 'z'
                l.append(ord(cell)-ord('a'))
            matrix.append(l)
    return min([BFS(matrix, x, end_coord) for x in start_coord])

def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>7.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")


if __name__ == "__main__":
    main()
