import time

def main():
    inputList = [1,0,16,5,17,4] # puzzle inputList
    #inputList = [0,3,6] 
    
    
    start = time.time()
    part1Answer = part1(inputList.copy())
    print(f"Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    start = time.time()
    part2Answer = part2(inputList)
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")
    
    
def part1(inputList):
    for turn in range(len(inputList)+1, 10):
        lastSaid = inputList[len(inputList)-1]
        count = inputList.count(lastSaid)
        #print(f"Turn {turn} and last spoken was: {lastSaid} and it was said {count}")
        #print(f"  List: {inputList}")
        if count == 1:
            index = 0
        else: 
            indices = [i for i, x in enumerate(inputList) if x == lastSaid]
            #print(indices)
            index = indices[-1] - indices[-2]
            #print(f"{index}")
        #print(f"\tAppending {index} to {inputList}")
        inputList.append(index)
        
        
        
    lastSaid = inputList[len(inputList)-1]
    print(inputList)
    return lastSaid
    
def part2(inputList):
    dct = {y: (-1 ,x) for (x,y) in enumerate(inputList, 1)}
    lastSaid = inputList[len(inputList)-1]
    for turn in range(len(inputList)+1, 30000001):
        (old, new) = dct[lastSaid]
        if old == -1:
            (old, new) = dct[0]
            dct[0] = (new, turn)
            lastSaid = 0
        else:
            (old, new) = dct[lastSaid]
            steps = new - old
            try:
                (a, b) = dct[steps]
                dct[steps] = (b, turn)
            except:
                dct[steps] = (-1, turn)
            lastSaid = steps
    return lastSaid
        
    
    
main()
