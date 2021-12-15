import time
import math

class Cell:
    def __init__(self, coord, points, adj) -> None:
        self.coord = coord
        self.points = points
        self.dist = math.inf if (coord != (0,0)) else 0
        self.adj = adj
        self.visited = False

    def __str__(self) -> str:
        return f"{f'(x={self.coord[0]:3}, y={self.coord[1]:3}) dist= {self.dist:5} p= {self.points} adj= |{self.adj}|':85}"

    def __repr__(self) -> str:
        return f"\n  {str(self)}\n"

    def set_dist(self, dist):
        self.dist = dist

    def set_visited(self):
        self.visited = True

    def get_coord(self):
        return self.coord

    def get_adj(self):
        return self.adj

    def get_points(self):
        return self.points

    def get_dist(self):
        return self.dist
    
    def is_visited(self):
        return self.visited


def get_adjacent_cells(x, y, neighbours, xmax=10, ymax=10):
    return [ (x + dx, y + dy) for dx, dy in neighbours if 0 <= (x + dx) < xmax and 0 <= y + dy < ymax ]


def solve(graph, max_x, max_y):
    start = time.time()
    to_visit = [graph[(0,0)]]

    while to_visit != []:
        cell  = to_visit.pop()
        print(f"Cell {cell} | {time.time()-start:.4f}s", end="\r")
        if cell.get_coord() == (max_x-1, max_y-1): #Max_x, max_y
            print()
            return cell
        for adj in cell.get_adj():
            new_dist = cell.get_dist() + graph[adj].get_points()
            if new_dist < graph[adj].get_dist():
                graph[adj].set_dist(new_dist)
                to_visit.append(graph[adj])
        cell.set_visited()
        to_visit.sort(key=lambda x: x.get_dist(), reverse=True)

        
def graph_maker(a, extend=1):
    org_size = (len(a), len(a[0]))
    extended_rows = []
    for row in a:
        new_row = [ 
            (cell+x) if cell+x <=9 else (cell+x)%9
            for x in range(9) for cell in row
        ]
        # for x in range(9):
        #     for cell in row:
        #         new_row.append((cell+x) if cell+x <=9 else (cell+x)%9)
        extended_rows.append(new_row)

    extended_grid = [[]]*org_size[0]*extend
    for j in range(org_size[0]):
        for i in range(extend):
            extended_grid[j+i*org_size[0]] = extended_rows[j][i*org_size[1]:i*org_size[1]+org_size[1]*extend]

    for row in extended_grid:
        print(row)

    max_y, max_x = (len(extended_grid), len(extended_grid[0]))
    graph = {}
    neighbours = [(1,0), (0, 1), (-1,0), (0, -1)]
    for r in range(max_y):
        for c in range(max_x):
            graph[(c,r)] = Cell((c, r), extended_grid[r][c], get_adjacent_cells(c,r, neighbours, max_x, max_y))
    return graph, max_x, max_y  


def main():
    with open("input.txt") as file:
        input_list = [[int(y) for y in x.strip()] for x in file.readlines()]
    
    # print("(1) What is the lowest total risk of any path from the top left to the bottom right?")
    # print(f"Answer: {solve(*graph_maker(input_list)).get_dist()}")
    # print("(2) What is the lowest total risk of any path from the top left to the bottom right?")
    # print(f"Answer: {solve(*graph_maker(input_list,5)).get_dist()}")
    graph_maker([[8]], 5)
    
main()
