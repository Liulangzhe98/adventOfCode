import time

def main():
    #f = open("input.txt", "r")
    #f = open("test.txt", "r")
    
    options = {}
    flag = -1
    error = 0
    valid = []
    mine = []
    start = time.time()
    #reading and part1
    with open('input.txt') as openfileobject:
        for line in openfileobject:
            timea = time.time()
            if line == "\n":
                continue
            elif line.startswith("your ticket"):
                flag = 1
                
            elif line.startswith("nearby"):
                flag = 2
            else:
                if flag == 1: #read your ticket
                    mine = line.strip().split(",")
                elif flag == 2: #read nearby tickets
                    validFlag = True
                    for value in line.split(","):
                        check = any([int(value) in x for x in options.values()])
                        if not check:
                            error += int(value)
                            validFlag = False
                    if validFlag:
                        valid.append(line.strip().split(","))
                        
                else: #first part
                    key = line.split(":")[0].strip()
                    ranges = line.split(":")[1].strip().split(" or ")
                    values = []
                    for r in ranges:
                        for i in range(int(r.split("-")[0]), int(r.split("-")[1])+1):
                            values.append(i)
                    #print(f"{key}: {values}")
                    options[key] = values
            print(f"per line takes: {flag} {(time.time()-timea)*1000:.2f}ms")
    
    part1Answer = error
    print(f"Reading and Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    
    
    #part2 
    start = time.time()
    taken = [0]*len(valid[0])
    slots = [""]*len(valid[0])
    

    while "" in slots:
        timeb = time.time()
        for i in range (len(valid[0])):
            if slots[i] == "":
                
                couldBe = [1]*len(valid[0])
                for x in valid:
                    check = [1 if int(x[i]) in option else 0 for option in options.values()]
                    couldBe = [a and b for a, b in zip(couldBe, check)]
                #print(f"pos{i} must be in {couldBe} {couldBe.count(1)}")
                
                possible = [a ^ b for a, b in zip(couldBe, taken)]
                if possible.count(1) == 1:
                    #print("SURE PLACEMENT")
                    taken[possible.index(1)] = int(1)
                    slots[i] = list(options.keys())[possible.index(1)]
        print(f"While loop takes: {(time.time()-timeb)*1000:.2f}ms")
    result = 1
    for x, option in enumerate( slots):
        if "departure" in option:
            result *= int(mine[x])

    part2Answer = result
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")
    
    

        
    
    
main()
