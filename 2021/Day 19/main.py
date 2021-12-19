import enum
import itertools
import re
import json
import math

from itertools import combinations, permutations
from collections import defaultdict

directions = [
        [ 1, 1, 1], # 0
        [ 1, 1,-1], # 1
        [ 1,-1, 1], # 1
        [-1, 1, 1], # 1
        [ 1,-1,-1], # 2
        [-1, 1,-1], # 2
        [-1,-1, 1], # 2
        [-1,-1,-1]
    ]


def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR
   
def tuple_diff(a, b):
    return tuple(map(lambda i, j: i-j, a, b))

def tuple_mult(a, b):
    return tuple(map(lambda i, j: i*j, a, b))

def tuple_sum(a, b):
    return tuple(map(lambda i, j: i+j, a, b))

def transform(coord, offset, new):
    print(f"  Transfrom {coord} with ", end ="")
    base =  [1, 10, 100]
    order = [abs(x) for x in offset]
    sign = [x//(abs(x)) for x in offset]
    # print(coord, offset, order, sign)
    if order == base:
        print(f"{offset}")
        if sign == [1, 1, 1]:
            return coord
        else:
            return tuple_mult(coord, sign)
    else:

        print(f"{new} && {offset}")
        coord = tuple_mult(coord, sign)
        b = (coord[1], coord[2], coord[0])
        print(b)
        # HAVE TO SWAP
        return b

def transform_all(beacons, rotation):
    output = []
    for beacon in beacons:
        output.append( 
            transform(beacon, rotation, None)
        )
        # print(beacon, transform(beacon, [-1,10,-100], None))
    return output

    
def scanner_overlap(base_list, scanner):
    coord_dict = defaultdict(int)
   
    for coord in scanner:
        for base in base_list:
            for p , q in zip(sequence(coord), sequence([1, 10, 100])):
                
                dist = (tuple(map(lambda i, j: i-j, base, p)))
                coord_dict[(dist, q)] += 1
    sorted_dict = {k: v for k, v in sorted(coord_dict.items(), key=lambda item: item[1])}
    k, v = list(sorted_dict.items())[-1]
    if v == 12:
        return k
    return None


def add_to_KB(KB, location, rotation, beacons):
    # rotation = [x//abs(x) for x in rotation]
    for coord in beacons:
        for p , q in zip(sequence(coord), sequence([1, 10, 100])):
            # print(q, rotation)
            if q == rotation:
                # print(f"{str(p):20} | {tuple_sum( p, location)}")
                KB.add(tuple_sum( p, location))

def new_KB(location, rotation, beacons):
    # rotation = [x//abs(x) for x in rotation]
    KB = set()
    for coord in beacons:
        for p , q in zip(sequence(coord), sequence([1, 10, 100])):
            # print(q, rotation)
            if q == rotation:
                # print(f"{str(p):20} | {tuple_sum( p, location)}")
                KB.add(tuple_sum( p, location))
    return KB

def main():
    EMPTY_COORD = [None, None, None] 
    with open("input.txt") as file:
        input_list = [[y for y in x.split("\n")[1:] if y != "" ] for x in file.read().split("\n\n")]
    scanners = []
    for scanner in input_list:
        scan = [ 
            tuple(map(int, beacon.strip().split(",")))
            for beacon in scanner
        ]
        scanners.append(scan)
    scanner_coord = dict([(x, EMPTY_COORD) for x in range(len(scanners))])
    scanner_coord[0] = [0,0,0]

    KB_dict = dict((x, set()) for x in range(len(scanners)))
    KB_dict[0] = set(scanners[0])
    visited = []
    counter = 0
    while True:
        print(f"While loop {counter} ", end="\r")
        keep_going = []
        can_visit = []
        for k, v in scanner_coord.items():
            if v != EMPTY_COORD and k not in visited:
                can_visit.append(k)
        for key in can_visit:
            visited.append(key)
            this_KB = KB_dict[key]

            for compare in range(len(scanners)):
                if compare in visited:
                    continue
                coord = scanner_overlap(this_KB, scanners[compare])
                # print(f"Comparing scanner[{compare}] to KB[{key}] resulted in {coord}")
                # print(len(scanners[compare]))
                # print(f"Scanner[{compare}] => {coord}")
                if coord != None:
                    # Found 12 overlapping beacons
                    # add_to_KB(KB, *coord, scanners[compare])
                    KB_dict[compare] = new_KB(*coord, scanners[compare])
                    scanner_coord[compare] = coord[0]

                    keep_going.append(True)
                else:
                    keep_going.append(False)
            visited.append(key)
        if not any(keep_going):
            print()
            break
        counter += 1
    all_set = set()
    for v in KB_dict.values():
        all_set.update(v)
    print(f"Part 1: {len(all_set)}")

    combs = list(combinations(range(len(scanners)), 2))
    max_man = 0
    for s1, s2 in combs:
        man = abs(sum(tuple_diff(scanner_coord[s1], scanner_coord[s2])))
        # print(s1, s2, man)
        max_man = max(man, max_man)
    print(f"Part 2: {max_man}")




main()
