def main():
    f = open("input.txt", "r")
    #f = open("test2.txt", "r")

    adapters = []
    for line in f.readlines():
        line = line.strip()
        adapters.append(int(line))
    adapters.append(0)
    adapters.sort(reverse = False)
    
    part1Answer = part1(adapters)
    part2Answer = part2(adapters)
    print(f"Part 1 is : {part1Answer} -> {part1Answer[0]*part1Answer[2]}")
    print(f"Part 2 is : {part2Answer}")

def part1(adapters):
    current = highest = max(adapters) + 3
        
    step = [1,2,3]
    done = [0,0,0]
    while not current == 0:
        for x in step:
            if (current-x) in adapters:
                current -= x
                done[x-1] += 1
                break
    return done


def part2(adapters):
    step = [1,2,3]
    
    waysdict = dict([(0,1)])
    
    for x in adapters[1:]:
        ways = 0
        for y in step:
            if x-y in waysdict.keys():
                ways += waysdict[x-y]
        waysdict[x] = ways
    out = waysdict[x]
    return out

main()
