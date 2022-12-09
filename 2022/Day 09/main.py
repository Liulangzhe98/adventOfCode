from copy import deepcopy
import math

def distance(H, T):
    return max(abs(H[0]-T[0]), abs(H[1]-T[1]))

def sign(x):
    return (x > 0) - (x < 0)

def tail_move(H, T):
    return (sign(H[0]-T[0]), sign(H[1]-T[1]))


def step(H, direction):
    return (H[0]+direction[0], H[1]+direction[1])


def tail_visits(head):
    visited_path = [(0,0)]
    T = (0, 0)
    for x in head:
        if distance(x, T) > 1:
            visited_path.append(T := step(T, tail_move(x,T)))
    return visited_path


def head_visited(text):
    visited = [(0,0)]
    H = (0,0)
    keys = {
        "U" : ( 1,0), # (R, C)
        "D" : (-1,0),
        "R" : (0, 1),
        "L" : (0,-1)
    }
    for line in text:
        direction, steps = line.strip().split()
        for i in range(int(steps)):
            visited.append(H := step(H, keys[direction]))

    return visited

def solve(file, tail_length=1):
    current_path = head_visited(file.readlines())
    visited_path = [(0,0)]
    for i in range(tail_length):
        visited_path = tail_visits(current_path)
        current_path = deepcopy(visited_path)
    return len(set(current_path))

def part_one(file_path):
    with open(file_path, 'r') as file:
        return solve(file)

def part_two(file_path):
    with open(file_path, 'r') as file:
        return solve(file, 9)

def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test2.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    
if __name__ == "__main__":
    main()
