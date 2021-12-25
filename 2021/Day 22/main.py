class Cuboid:
    def __init__(self, string: list = None, coords: tuple = None) -> None:
        if coords == None:
            self.coords = tuple(map(self.parse_range, string.split(",")))
        else:
            self.coords = coords

    def __str__(self) -> str:
        return f"Cube at : {self.coords}"

    def __repr__(self) -> str:
        return str(self)

    def intersect(self, other):
        # max of starts -> most right of starts
        # min of ends -> most left of ends
        return tuple(range(max(b.start, o.start),
                       min(b.stop, o.stop))
                 for b, o in zip(self.coords, other.coords))

    def volume(self):
        x, y, z = tuple(map(len, self.coords))
        return x*y*z

    def parse_range(self, s):
        c0, c1 = s[2:].split('..')
        return range(int(c0), int(c1)+1)

def part_one(commands):
    matrix = [[[0 for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)]
    counter = 0
    for state, target in commands:
        x1, x2, y1, y2, z1, z2 = [ 
                int(b) for a in target.split(",") for b in a[2:].split("..")
            ]
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





def unique_cuboid_volume(cuboid, rest):
    all_intersections = []
    for state, other in rest:
        intersection = Cuboid(coords=cuboid.intersect(other))
        if intersection.volume() > 0: # only add intersections
            all_intersections.append((state, intersection))
    volume = cuboid.volume()
    for idx, (_, intersection) in enumerate(all_intersections):
        volume -= unique_cuboid_volume(intersection, all_intersections[idx+1:])
    return volume


def part_two(commands):
    steps = []
    counter = 0
    for state, target in commands:
        cuboid = Cuboid(string=target)
        steps.append((state, cuboid))
    
    for idx, (state, cuboid) in enumerate(steps):
        if state == "on":
            counter += unique_cuboid_volume(cuboid, steps[idx+1:])
    return counter
    

def main():
    with open("input.txt") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
   
    print("(1) How many cubes are on?")
    print(f"Answer: {part_one(lines)}")
    print("(2) How many cubes are on?")
    print(f"Answer: {part_two(lines)}")


main()
