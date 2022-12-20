def m_dist(a, b):
    return sum([abs(i-j) for i, j in zip(a,b)])

def part_one(file_path):
    with open(file_path, 'r') as file:
        coords = []
        for line in file.read().splitlines():
            coords.append(list(map(int, line.split(","))))
        total = 6*len(coords)
        for e, first in enumerate(coords, 1):
            for second in coords:
                total -= (m_dist(first, second) == 1)
    return total


def part_two(file_path):
    bounds = [
        (0, 0),
        (0, 0),
        (0, 0)
    ]

    with open(file_path, 'r') as file:
        coords = []
        for line in file.read().splitlines():
            blub = tuple(map(int, line.split(",")))
            coords.append(blub)
            for e, c in enumerate(blub):
                bounds[e] = (min(bounds[e][0], c), max(bounds[e][1], c))

        for i in range(len(bounds)):
            bounds[i] = (bounds[i][0]-1, bounds[i][1]+1)

        q = [(0,0,0)]
        visited = []
        touchy = 0
        while q:
            x, y, z = q.pop(0)
            c = (x, y, z)
            if (x, y, z) in visited:
                continue
            visited.append((x, y, z))
            guards = [(0, x-1), (0, x+1), (1, y-1), (1, y+1), (2, z-1), (2, z+1)]
            for a, g in guards:
                if bounds[a][0] <= g <= bounds[a][1]:
                    new = tuple([c[i] if i != a else g for i in range(3)])
                    if new in coords:
                        touchy += 1
                    else:
                        q.append(new)
        return touchy


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    
if __name__ == "__main__":
    main()
