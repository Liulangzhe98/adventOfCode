def distance(H, T):
    return max(abs(H[0]-T[0]), abs(H[1]-T[1]))


def sign(x):
    return (x > 0) - (x < 0)


def tail_move(H, T):
    return (sign(H[0]-T[0]), sign(H[1]-T[1]))


def step(H, direction):
    return (H[0]+direction[0], H[1]+direction[1])


def tail_visits(head):
    return [T := (0, 0)] + [T := step(T, tail_move(x, T)) for x in head if distance(x, T) > 1]


def head_visited(text):
    keys = {
        "U": (1, 0),  # (R, C)
        "D": (-1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    return [H := (0, 0)] + [
        H := step(H, keys[d])
        for d, steps in [line.split() for line in text.splitlines()]
        for _ in range(int(steps))
    ]


def solve(file, tail_length=1):
    current_path = head_visited(file.read())
    for i in range(tail_length):
        current_path = tail_visits(current_path)
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
