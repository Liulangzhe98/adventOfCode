# x -> left, right
# y -> up, down
# z -> forward, backward

from typing import Set


class Cube:
    def __init__(self, coords:list, type=0) -> None:
        self.coords = coords
        self.type = type # 0 = OFF, 1 = ON
        self.volume = volume_cube(self.coords)

    def set_type(self, type):
        self.type = type

    def __str__(self) -> str:
        return f"{self.coords} = {'ON' if self.type else 'OFF':3} => {self.volume}"
    
    def __repr__(self) -> str:
        return str(self)

    def intersection(self, other):
        # print(f"Compare S:{self} \n\tO:{other}")
        c_s = self.coords
        c_o = other.coords

        orient = [
            [None, None], [None, None], [None, None]
        ]
        for i in range(3):
            if c_s[i*2] >= c_o[i*2]:
                orient[i][0] = ["R", "U", "B"][i]
                if c_s[i*2] <= c_o[i*2+1]:
                    orient[i][1] = (c_s[i*2], min(c_s[i*2+1], c_o[i*2+1]))
            else:
                orient[i][0] = ["L", "D", "F"][i]
                if c_s[i*2+1] <= c_o[i*2+1]:
                    orient[i][1] = (max(c_s[i*2], c_o[i*2]), c_s[i*2+1])
        if not all([x[1] != None for x in orient]):
            return None
        # print(orient)
        if orient[0][0] == "L":
            x_set = [orient[0][1][0], c_s[1]]
        else:
            x_set = [c_s[0], orient[0][1][1]]
        if orient[1][0] == "D":
            y_set = [orient[1][1][0], c_s[3]]
        else:
            y_set = [c_s[2], orient[1][1][1]]
        if orient[2][0] == "F":
            z_set = [orient[2][1][0], c_s[5]]  
        else:
            z_set = [c_s[4], orient[2][1][1]]

        intersect = Cube(
                x_set + y_set + z_set
            )
        if self.type == 1:
            return ("Double On", intersect)
        else:
            return ("Turned Off", intersect)        



def part_one(commands):
    matrix = [[[0 for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)]
    counter = 0
    for state, target in commands:
        x1, x2, y1, y2, z1, z2 = [ 
                int(b) for a in target.split(",") for b in a[2:].split("..")
            ]
        #check within bounds
        if (x2 < -50 or x1 > 50 or y2 < -50 or y1 > 50 or z2 < -50 or z1 > 50):
            continue
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    if state == "on":   
                        counter += (1-matrix[x][y][z])
                        matrix[x][y][z] = 1
                    else:
                        counter -= matrix[x][y][z]
                        matrix[x][y][z] = 0
    return counter

def cube_comp(new_cube, e_cube):
    print(f"Compare {new_cube} and {e_cube}")

    if (new_cube[0] >= e_cube[0] and new_cube[0] <= e_cube[1]):
        # print("WITHIN SAME X-axis")
        if new_cube[2] >= e_cube[2] and new_cube[2] <= e_cube[3]:
            # print("WITHIN SAME Y-axis")
            if new_cube[4] >= e_cube[4] and new_cube[4] <= e_cube[5]:
                # print("INTERSECTION")
                return  (new_cube[0], min(new_cube[1], e_cube[1]),
                         new_cube[2], min(new_cube[3], e_cube[3]), 
                         new_cube[4], min(new_cube[5], e_cube[5]))
    
def volume_cube(cube):
    return (cube[1]+1-cube[0])*(cube[3]+1-cube[2])*(cube[5]+1-cube[4])


def part_two(commands):
    cubes = []
    doubles = []
    turn_off = []
    for state, target in commands:
        next_cube = Cube([ int(b) for a in target.split(",") for b in a[2:].split("..")], type=state=="on")
        print(next_cube)
        new_lid = next_cube.volume
        for cube in cubes:
            
            result = next_cube.intersection(cube)
            print(result)
            if result != None:
                if result[0] == "Double On":
                    new_lid -= result[1].volume
                    doubles.append(result[1])
                if result[0] == "Turned Off":
                    
                    turn_off.append(result[1])
        print(next_cube, new_lid)
        if next_cube.type == 1:
            cubes.append(next_cube)



        print("="*30)

    print(f"Volume: {sum([x.volume for x in cubes])-sum(x.volume for x in doubles)}")
            

               
    # print(cuboid_on)
    # print(cuboid_off)
    # counter = 0
    # for cube in cuboid_on:
    #     counter += volume_cube(cube)
    # for cube in cuboid_off:
    #     counter -= volume_cube(cube)
    # print(f"Volume: {counter}")



            
    




def main():
    with open("test_small.txt") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
   
    print("(1) How many cubes are on?")
    print(f"Answer: {part_one(lines)}")
    # print("(2) Find the player that wins in more universes; in how many universes does that player win?")
    print(f"Answer: {part_two(lines)}")

    print("#"*75)
    with open("test_anne.txt") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
   
    print("(1) How many cubes are on?")
    print(f"Answer: {part_one(lines)}")
    # print("(2) Find the player that wins in more universes; in how many universes does that player win?")
    print(f"Answer: {part_two(lines)}")


main()
