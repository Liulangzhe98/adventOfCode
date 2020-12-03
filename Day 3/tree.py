import math


def main():
    file = open("input.txt", "r")

    counter = 0
    treesPart1 = 0
    counterList = [0,0,0,0,0]
    trees = [0,0,0,0,0]
    
    options = [1, 3, 5, 7, 1]

    skipRowFlag = False
  
    for line in file.readlines():
        line = line.strip()
        # Part 1
        treesPart1 += line[counter%len(line)] == '#'
        counter += 3
        
        # Part 2
        for i in range(len(trees)):
            if i == (len(trees)-1) and skipRowFlag:
                skipRowFlag = False
            else:
                charPoint = (counterList[i])%len(line)
                trees[i] += line[charPoint] == '#'
                counterList[i] += options[i]
                if i == (len(trees) -1):
                    skipRowFlag = True
    print(f"Part 1: Total trees hit: {treesPart1}")
    print(f"Part 2: Total trees hit: {trees} | {math.prod(trees)}" )

main()
