import time
import re

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

def main():
    start = time.time()
    f = open("input.txt", "r")
    #f = open("test.txt", "r")
   
    start = time.time()
    part1Answer = part1(f)
    print(f"Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    start = time.time()
    f = open("input.txt", "r")
    part2Answer = part2(f)
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")
    
    
def part1(f):
    memory = {}
    line = f.readline().strip()
    mask = ""
    while line:
        if line.startswith("mask"):
            mask = line.split(" = ")[1] 
        else:
            instruction = [int(s) for s in re.findall(r'\d+', line)]
            binIns = format(instruction[1], 'b').zfill(36)
            binList = Convert(binIns)
            for count, m in enumerate(mask):
                if not m == 'X':
                    binList[count] = m
            binIns = "".join(binList)
            memory[instruction[0]] = int(binIns, 2)
        line = f.readline().strip()
    return(sum(memory.values()))
    
    
def part2(f):
    memory = {}
    line = f.readline().strip()
    mask = ""
    while line:
        if line.startswith("mask"):
            mask = line.split(" = ")[1] 
        else:
            instruction = [int(s) for s in re.findall(r'\d+', line)]
            binIns = format(instruction[0], 'b').zfill(36)
            binList = Convert(binIns)
            for count, m in enumerate(mask):
                if not m == '0':
                    binList[count] = m
            solutions = generateBitString("".join(binList))
            
            binIns = "".join(binList)
            for slot in solutions:
                memory[slot] = instruction[1]
        line = f.readline().strip()
    return(sum(memory.values()))

def generateBitString(bitList):
    out = []
    total = [bitList]
    check = any(['X' in item for item in total])
    while check:
        for item in total:
            if 'X' in item:
                copy = copy2= item
                total.append(copy.replace('X', '0', 1))
                total.append(copy2.replace('X', '1', 1))
                total.remove(item)
        check = any(['X' in item for item in total])
    for string in total:
        out.append(int(string,2))
    return out

main()
