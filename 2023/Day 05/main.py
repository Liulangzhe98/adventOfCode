from collections import namedtuple
from itertools import islice
from dataclasses import dataclass

mapping = namedtuple('Mapping', ['left', 'right', 'diff'])

@dataclass(order=True)
class SeedPair:
    l: int
    r: int


def move_seed(seed: int, pairs: mapping) -> int:
    for pair in pairs:
        if pair.left <= seed <= pair.right:
            return seed + pair.diff
    return seed

def move_seed_complex(seeds: SeedPair, pairs: mapping) -> tuple[list, list]:
    for pair in pairs:
        # Seed range is outside of mapping, so skip to next mapping
        if seeds.l > pair.right or seeds.r < pair.left:
            continue
        # Seed range is inside of mapping
        if seeds.l >= pair.left and seeds.r <= pair.right:
            c, f = [], [SeedPair(seeds.l+pair.diff, seeds.r+pair.diff)]
            return c,f
        # Seed range encapsulate the mapping
        if seeds.l < pair.left and seeds.r > pair.right:
            c,f = [SeedPair(seeds.l, pair.left-1), SeedPair(pair.right+1, seeds.r)] , [SeedPair(pair.left+pair.diff, pair.right+pair.diff)]
            return c, f
        # Seed range falls over left boundary of mapping
        if seeds.l < pair.left and pair.left <= seeds.r <= pair.right:
            c, f =  [SeedPair(seeds.l, pair.left-1)], [SeedPair(pair.left+pair.diff, seeds.r+pair.diff)]
            return c, f
        # Seed range falls over right boundary of mapping
        if seeds.r > pair.right and pair.left <= seeds.l <= pair.right:
            c, f =  [SeedPair(pair.right+1, seeds.r)], [SeedPair(seeds.l+pair.diff, pair.right+pair.diff)]
            return c, f
    return [], [seeds]


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def part_one(file_path):
    with open(file_path, 'r') as file:
        blocks = file.read().strip().split("\n\n")

        seeds = sorted([int(x) for x in blocks[0].split(": ")[1].split()])

        for block in blocks[1:]:
            pairs = []
            # Create all mappings
            for line in block.split("\n")[1:]:
                dest, src, length = [int(x) for x in line.split()]
                pairs.append(mapping(left=src,right= src+length, diff=dest-src))
        
            # Move seeds accordingly
            seeds = [move_seed(seed, pairs) for seed in seeds]
    return min(seeds) 


def part_two(file_path):
    with open(file_path, 'r') as file:
        blocks = file.read().strip().split("\n\n")

        seeds = [int(x) for x in blocks[0].split(": ")[1].split()]
        batched_seeds = batched(seeds, 2)
        current = []
        for l, r in batched_seeds:
            a = SeedPair(l, l+r)
            current.append(a)
        for block in blocks[1:]:
            pairs = []
            # Create all mappings
            for line in block.split("\n")[1:]:
                dest, src, length = [int(x) for x in line.split()]
                pairs.append(mapping(left=src,right= src+length, diff=dest-src))
        
            # Move seeds accordingly
            following = []
            while next_pair := current.pop(0):
                c, f = move_seed_complex(next_pair, pairs)
                current += c
                following += f
                if current == []:
                    break
            current = following.copy()
    return sorted(current)[0].l 

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
