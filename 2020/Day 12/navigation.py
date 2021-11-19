import time

def main():
    start = time.time()
    f = open("input.txt", "r")
    #f = open("test.txt", "r")
    instructions = []
    for line in f.readlines():
        line = line.strip()
        direction = line[:1]
        amount = int(line[1:])
        instructions.append((direction, amount))
   
    print(f"Reading took: {(time.time()-start)*1000:.2f}ms")
   
    start = time.time()
    part1Answer = part1(instructions)
    print(f"Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    start = time.time()
    part2Answer = part2(instructions)
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")

def part1(instructions):
    options = ["North", "East", "South", "West"]
    facing = 1
    location = [0,0] # (north, east)
    for (direction, amount) in instructions:
        if direction == "N":
            location[0] += amount
        if direction == "S":
            location[0] -= amount
        if direction == "E":
            location[1] += amount
        if direction == "W":
            location[1] -= amount
            
        if direction == "L":
            facing = (facing - amount//90)%4
        if direction == "R":
            facing = (facing + amount//90)%4
        if direction == "F":
            location[facing%2] += (-amount if facing > 1 else amount)
    return sum(abs(x) for x in location)

def part2(instructions):
    options = ["North", "East", "South", "West"]
    location = [0,0] # [east, north]
    waypoint = [10, 1] # [east, north]
    for (direction, amount) in instructions:
        if direction == "N":
            waypoint[1] += amount
        if direction == "S":
            waypoint[1] -= amount
        if direction == "E":
            waypoint[0] += amount
        if direction == "W":
            waypoint[0] -= amount
            
        if direction == "L":
            steps = amount//90
            for i in range(0, steps):
                waypoint = [-waypoint[1], waypoint[0]]
        if direction == "R":
            steps = amount//90
            for i in range(0, steps):
                waypoint = [waypoint[1], -waypoint[0]]
        if direction == "F":
            location[0] += waypoint[0]*amount
            location[1] += waypoint[1]*amount
    return sum(abs(x) for x in location)
main()
