import copy

result = """#############
#..*.*.*.*..#
###A#B#C#D###
  #A#B#C#D#
  #########"""


class Amphipod_Hotel:
    def __init__(self, tiles) -> None:
        self.tiles = tiles
        self.key = "".join([x.state for x in self.tiles])
    
    def __str__(self) -> str:
        return f"{self.key}"

    def __repr__(self) -> str:
        return str(self)

    def print_rooms(self):
        row = 0
        for x in self.tiles:
            if x.coord[0] != row:
                print()
                row += 1
            print(x.state, end="")
        print()
       
class Tile:
    def __init__(self, coord, state) -> None:
        self.coord = coord
        self.state = state

    def __str__(self) -> str:
        return f"{self.coord} -> {self.state}"

    def __repr__(self) -> str:
        return f"{str(self)}"



def part_one():
    pass


def part_two():
    pass


WALL = ["#", " ", "*"]
AMPHIPODS = "ABCD"
FREE = "."

import time


def create_path(src, dest):
    s_y, s_x = src
    d_y, d_x = dest
    (y, x) = src
    path = []
    for y in range(s_y-1, 0, -1):
        path.append((y, s_x))
    move_left = (s_x > d_x)
    if move_left:
        for x in range(s_x-1, d_x-1, -1):
            path.append((y, x))
    else:
        for x in range(s_x+1, d_x+1):
            path.append((y, x))
    if (y, x) != dest:
        path.append(dest)
    return path


def check_path(state, path, matrix):
    for coord in path:
        for tile in [x for x in matrix.tiles if x.state in AMPHIPODS]:
            if coord == tile.coord:   
                return False
        if coord[0] == 2:
            if state != list(filter(lambda x: x.coord == (3, coord[1]), matrix.tiles))[0].state:
                return False
    return True


def do_move(matrix, src, dest, state):
    matrix_new = copy.deepcopy(matrix)
    idx_src =  matrix.tiles.index(src)
    dest_tile = list(filter(lambda x: x.coord == dest, matrix.tiles))[0]
    idx_dest = matrix.tiles.index(dest_tile)
    
    matrix_new.tiles[idx_dest].state = src.state
    matrix_new.tiles[idx_src].state = dest_tile.state
    matrix_new.key = "".join([x.state for x in matrix_new.tiles])
    return matrix_new


def BFS(matrix, goal, cost):
    Q = [(0, matrix)]
    visited = []
    while Q != []:
        # time.sleep(1)
        Q.sort(key=lambda x: x[1].cost)
        cost, v = Q.pop(0)
        # print(v.__hash__())
        print(f"Est: {v.cost:6}, move till here: {cost:6} = {v.cost+cost:8}", end ="\r")
        if v.__hash__() == goal.__hash__():
            print(f"Found a min at: {v.cost:6}, move till here: {cost:6} = {v.cost+cost}")
            # exit()

        if v.__hash__() in visited:
            continue
        visited.append(v.__hash__())
        
        for move in [x for x in v.tiles if x.state in AMPHIPODS]:
            # print(f"Tile {move} could move to :")
            # print("="*30)
            if move.coord in amphi_dict[move.state][1]:
                if move.coord[0] == 3:
                    # print("  I WONT MOVE")
                    continue
                if move.coord[0] == 2:
                    b = list(filter(lambda x: x.coord == (3, move.coord[1]), v.tiles))[0].state == move.state
                    if b:
                        # print(f"  Rooms for amphipod {move.state} is done")
                        continue
            for dest in amphi_dict[move.state][1]+HALLWAY:
                if dest[0] == 1 and move.coord[0] == 1:
                    continue
                path = create_path(move.coord, dest)

                can_walk = check_path(move.state, path, v)
                # print(f"  {move} --> Dest: {dest} {path if can_walk else 'not'}")
                if can_walk: 
                    move_cost = (len(path)*amphi_dict[move.state][0])
                    m_new = do_move(v, move, dest, move.state)
                    Q.append((cost+move_cost, m_new))


def cost_from_path(path):
    return sum((int(x.split(":")[-1].strip()) for x in path))

import math



def dijkstra(matrix, goal):
    cloud_KB = {}
    possible = []
    cost = 0
    visited = []
    visiting = matrix
    while visiting.key != goal.key:
        visited.append(visiting.key)
        time.sleep(1)
        print(visiting.key)
        for move in [x for x in matrix.tiles if x.state in AMPHIPODS]:
            if move.coord in amphi_dict[move.state][1]:
                if move.coord[0] == 3:
                    continue
                if move.coord[0] == 2:
                    b = list(filter(lambda x: x.coord == (3, move.coord[1]), matrix.tiles))[0].state == move.state
                    if b:
                        continue
            for dest in amphi_dict[move.state][1]+HALLWAY:
                if dest[0] == 1 and move.coord[0] == 1:
                    continue
                path = create_path(move.coord, dest)

                can_walk = check_path(move.state, path, matrix)
                # print(f"  {move} --> Dest: {dest} {path if can_walk else 'not'}")
                if can_walk: 
                    move_cost = (len(path)*amphi_dict[move.state][0])
                    m_new = do_move(matrix, move, dest, move.state)
                    if not cloud_KB.get(m_new.key):
                        cloud_KB[m_new] = [cost + move_cost, False]
                    else:
                        cloud_KB[m_new] = [min(cloud_KB[m_new], cost+move_cost), cloud_KB[m_new][1]]
        #             # print(f"Adding: {m_new} to possible")
        #             possible.append((move_cost, m_new))
        
        # possible.sort(key=lambda x: x[0])
        # possible = list(filter(lambda x: x[1].key not in visited, possible))
        # visited.append(visiting.key)
        # cost, visiting = possible.pop(0)
       
        cloud_KB = {k: v for k, v in sorted(cloud_KB.items(), key=lambda item: item[1])}
        
        for k, v in cloud_KB.items():
            if v[1] == False:
                
                visiting = k
                cost = v[0]
                cloud_KB[k] = [cost, True]
                break

        
    # print(possible)
    pass




HALLWAY = [(1, 1), (1, 2), (1,4), (1, 6), (1,8), (1,10), (1,11)]


amphi_dict = {
    "A": (1, [(2, 3), (3,3)]), 
    "B": (10, [(2, 5), (3,5)]),
    "C": (100, [(2, 7), (3,7)]),
    "D": (1000, [(2, 9), (3,9)]),
}


def main():
    with open("test_fixed.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
    
    
    goal = Amphipod_Hotel([
        Tile((r, c), char)
        for r, row in enumerate(result.splitlines())
        for c, char in enumerate(row)
    ])
    print(goal.key)
    print("===============")


    matrix = Amphipod_Hotel([
        Tile((r, c), char )
        for r, row in enumerate(lines)
        for c, char in enumerate(row)
    ])
    print(matrix.print_rooms())
    # print(matrix.estimated())
    dijkstra(matrix, goal)






    # BFS(matrix, goal, 0)
    # print(movable)


    # print("(1) What do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?")
    # print(f"Answer: {part_one()}")
    # print("(2) Find the player that wins in more universes; in how many universes does that player win?")
    # print(f"Answer: {part_two()}")
main()
