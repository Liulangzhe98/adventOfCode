import re

class Sensor(object):
    def __init__(self, x, y, dist):
        super(Sensor, self).__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def in_range(self, x, y):
        return m_dist(self.x, self.y, x, y) <= self.dist

    def can_see(self, y):
        if self.y == y:
            return True
        if self.y > y:
            return self.y - self.dist <= y
        return self.y + self.dist >= y

    def width(self, y):
        if self.can_see(y):
            pass
            d = self.dist-abs(self.y-y)
            return (self.x- d, self.x+d)
            return ("CAN SEE", abs(self.y -y))
        else:
            return None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Sensor {(self.x, self.y)} with dist = {self.dist}"
        

def m_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def overlap(ranges, max_xy):
    ranges.sort(key=lambda x: x[0])
    flag = True
    bound_min = 0
    bound_max = 0
    for (begin, end) in ranges:
        if flag:
            if begin > bound_min:
                return (False, 0)
            bound_max = max(bound_max, end)
            flag = False
        if begin-1 > bound_max:
            return (False, bound_max+1)
        bound_max = max(bound_max, end)
    return (bound_max >= max_xy, None)


def part_one(file_path, y):
    sensors = []
    beacons = set()
    
    bound_min = 0
    bound_max = 0
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            sx, sy, bx, by = map(int, re.findall( "([-\d+]+)", line))
            dist = m_dist(sx, sy, bx, by )
            bound_min = min(bound_min, sx-dist-1)
            bound_max = max(bound_max, sx+dist+1)
            s = Sensor(sx, sy, dist)
            if s.can_see(y):
                sensors.append(s)
            beacons.add((bx, by))

    count = any([s.in_range(0, y) for s in sensors])

    r = max(abs(bound_min), bound_max)
    for i in range(1, r):
        # if i % (r//20) == 0 and i > 0:
        #     print(f"At {i/r:.2%}")
        count += any([s.in_range(i, y) for s in sensors]) 
        count += any([s.in_range(-i, y) for s in sensors])
    return count-len(list(filter(lambda x: x[1] == y, beacons)))


def part_two(file_path, max_xy):
    sensors = []
    beacons = set()
    
    bound_min = 0
    bound_max = 0
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            sx, sy, bx, by = map(int, re.findall( "([-\d+]+)", line))
            dist = m_dist(sx, sy, bx, by )
            bound_min = min(bound_min, sx-dist-1)
            bound_max = max(bound_max, sx+dist+1)
            s = Sensor(sx, sy, dist)
            sensors.append(s)
            beacons.add((bx, by))

    for y in range(max_xy):
        # if y % (max_xy//20) == 0 and y > 0:
        #     print(f"At {y/max_xy:.2%}")

        overlap_r = []
        for s in sensors:
            if (r := s.width(y)): # Make the 0 a for loop
                overlap_r.append(r)
                # print(" ",s, r)
        result = overlap(overlap_r, max_xy)
        if result[0] == False:
            # print(f"Y[{y}]: {result}")
            return result[1]*4000000+y
       
    # offset = max_xy//2
    # for x in range(offset):
    #     print(x, x+offset)

def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(*file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, ("test.txt", 10))
    timed_print("Solution 2T", part_two, ("test.txt", 20))
    timed_print("Solution 1 ", part_one, ("input.txt", 2000000)) #Solution 1  took 109813.04ms : 4725496 
    timed_print("Solution 2 ", part_two, ("input.txt", 4000000)) #Solution 2  took  85016.89ms : 12051287042458 

    
if __name__ == "__main__":
    main()
