from collections import defaultdict

def part_one(file_path):
    with open(file_path, 'r') as file:
        layer = set()
        summation = 0
        for e, line in enumerate(file.read().strip().splitlines()):
            new_layer = set()
            if 'S' in line:
                layer = {line.index('S')}
            else:
                indices = [i for i, x in enumerate(line) if x == "^"]
                if not indices:
                    continue
                for i in indices:
                    if i in layer:
                        new_layer.add(i-1)
                        new_layer.add(i+1)
                        summation += 1
                left_over = (layer - set(indices))
                layer = new_layer | left_over
    return summation


def part_two(file_path):
    with open(file_path, 'r') as file:
        front = defaultdict(int)
        for e, line in enumerate(file.read().strip().splitlines()):
            new_front = defaultdict(int)
            if 'S' in line:
                front[line.index("S")] = 1
            else:
                indices = [i for i, x in enumerate(line) if x == "^"]
                if not indices:
                    continue
                for p, v in front.items():
                    if p in indices:
                        new_front[p+1] += indices.count(p) * v
                        new_front[p-1] += indices.count(p) * v
                    else:
                        new_front[p] += front[p]
                front = new_front
    return sum(front.values())


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
