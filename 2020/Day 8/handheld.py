def main():
    lineNr = 0
    instructions = []     
    f = open("input.txt", "r")
    #f = open("test.txt", "r")
    #parser
    for line in f.readlines():
        triplet = (line.strip().split(" "), lineNr)
        
        instructions.append(triplet)
        lineNr += 1
    #part 1
    (acc, fin) = checkInfLoop(instructions)
    
    #part 2
    (part2, changed) = fixInfLoop(instructions)

    print(f"Part 1 is : {acc}")
    print(f"Part 2 is : {part2}")
    print(f"\tFound by changing instructions[{changed}]")
    print(f"\t{instructions[changed]}")
    
def checkInfLoop(instructions): 
    acc = 0
    current = 0
    visited = []
    #part 1
    #keep looping until we reach the and or untill an instructions is found that was alredy visited
    while current < len(instructions) and not instructions[current] in visited:
        visited.append(instructions[current])
        (ins, amount), lineNr = instructions[current]
        if ins == "acc":
            acc += int(amount)
            current += 1
        elif ins == "jmp":
            current += int(amount)
        else: #no operator
            current += 1   
    fin = current < len(instructions)
    return (acc, fin)

def fixInfLoop(instructions):
    for i, ((ins, amount), lineNr) in enumerate(instructions):
        copy = instructions.copy() #need the .copy() otherwise the instructions are also changed
        if ins == "jmp":
            # change a jmp instruction to a no op and check if we can reach the end of the instructions
            copy[i] = ['nop', amount], lineNr
            (acc, fin) = checkInfLoop(copy)
            if fin == 0:
                return (acc, i)
    # no solution
    return (0, -1)

    
    
    

main()
