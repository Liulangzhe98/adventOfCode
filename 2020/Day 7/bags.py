def main():

    #f = open("test.txt", "r")
    #f = open("input_anne.txt", "r")
    f = open("input.txt", "r")
    
    #reading the input
    bagOfHolding = []
    for line in f.read().splitlines():
        line = line[:-1]
        bag = line.split("bags")[0].strip()
        if ',' in line:
            innerBags = []
            for inside in line.split("contain")[1].split(','):
                innerBags.append(inside.strip())
        else:
            innerBags = [line.split("contain")[1].strip()]
        bagOfHolding.append( (bag, innerBags))

    #part 1
    search = ["shiny gold"]
    prevCount = 0
    count = len(search)
    while not prevCount == count:
        for bag in bagOfHolding:
            check = any(word in a for word in search for a in bag[1])
            if check:
                if not bag[0] in search:
                    search.append(bag[0])
        prevCount = count
        count = len(search)
       
    #part 2
    part2 = countBags(bagOfHolding, "shiny gold", 1)

    print(f"Result of part1 is: {len(search)-1}")
    print(f"Result of part2 is: {part2-1}")


def countBags(bags, search, multiplier):
    out = 0
    for bag in bags:
        check = search == bag[0]
        if check:
            if "no other bags" in bag[1]:
                return multiplier
            for inner in bag[1]:
                deeper = countBags(bags, inner[2:-4].strip(), int(inner[:2]))
                out +=  deeper 
    out = multiplier + out*multiplier
    return out
    

main()
