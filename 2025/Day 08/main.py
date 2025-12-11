import math

def part_one(file_path, loops):
    with open(file_path, 'r') as file:
        coords = []
        for line in file.read().strip().splitlines():
            coords.append([int(x) for x in line.split(",")])
        
        distances = []
        for e, c in enumerate(coords[:-1]):
            for nc in coords[e+1:]:
                d = math.sqrt((c[0]-nc[0])**2 + (c[1]-nc[1])**2 + (c[2]-nc[2])**2)
                distances.append([c, nc, d])
        distances.sort(key=lambda x: x[2])
        circuits = []
        checked = 0
        for c1, c2, _ in distances[:loops]:
            c1_set = next(filter(lambda x: str(c1) in x, circuits), None)
            c2_set = next(filter(lambda x: str(c2) in x, circuits), None)
            if c1_set and c2_set:
                if c1_set == c2_set:
                    continue
                circuits.remove(c1_set)
                circuits.remove(c2_set)
                c1_set |= c2_set
                circuits.append(c1_set)
            elif c1_set:
                circuits.remove(c1_set)
                c1_set.add(str(c2))
                circuits.append(c1_set)
            elif c2_set:
                circuits.remove(c2_set)
                c2_set.add(str(c1))
                circuits.append(c2_set)
            elif not (c1_set and c2_set):
                circuits.append({str(c1), str(c2)})
        a = sorted([len(c) for c in circuits], reverse=True)
    return math.prod(a[:3]) 


def part_two(file_path, loops):
    with open(file_path, 'r') as file:
        coords = []
        circuits = []
        for line in file.read().strip().splitlines():
            a = [int(x) for x in line.split(",")]
            coords.append(a)
            circuits.append({str(a)})

        distances = []
        for e, c in enumerate(coords[:-1]):
            for nc in coords[e+1:]:
                d = math.sqrt((c[0]-nc[0])**2 + (c[1]-nc[1])**2 + (c[2]-nc[2])**2)
                distances.append([c, nc, d])
        distances.sort(key=lambda x: x[2])
        for c1, c2, _ in distances:
            c1_set = next(filter(lambda x: str(c1) in x, circuits), None)
            c2_set = next(filter(lambda x: str(c2) in x, circuits), None)
            if c1_set and c2_set:
                if c1_set == c2_set:
                    continue
                circuits.remove(c1_set)
                circuits.remove(c2_set)
                c1_set |= c2_set
                circuits.append(c1_set)
            elif c1_set:
                circuits.remove(c1_set)
                c1_set.add(str(c2))
                circuits.append(c1_set)
            elif c2_set:
                circuits.remove(c2_set)
                c2_set.add(str(c1))
                circuits.append(c2_set)
           
            a = sorted([len(c) for c in circuits], reverse=True)
            if not 1 in a:
                break
    return c1[0]*c2[0]


def timed_print(text, func, file, loops):
    import time
    start = time.time()
    result = func(file, loops)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt", 10)
    timed_print("Solution 2T", part_two, "test.txt", 10)
    timed_print("Solution 1 ", part_one, "input.txt", 1000)
    timed_print("Solution 2 ", part_two, "input.txt", 1000)
    

if __name__ == "__main__":
    main()
