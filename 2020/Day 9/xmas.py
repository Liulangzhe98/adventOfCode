def main():
    f = open("input.txt", "r")
    #f = open("test.txt", "r")
    
    SIZE = 25
    
    listOfNumber = []
    for line in f.readlines():
        listOfNumber.append(int(line.strip()))
        
    part1Answer = part1(listOfNumber, SIZE)
    part2Answer = part2(listOfNumber, part1Answer)
    print(f"Part 1 is : {part1Answer}")
    print(f"Part 2 is : {part2Answer}")
    
    


def part1(listOfNumber, SIZE):
    for i in range(0, len(listOfNumber)-SIZE):
        #print(f"Preamble: {listOfNumber[i:i+SIZE]} -> {listOfNumber[i+SIZE]}")
        preamble = listOfNumber[i:i+SIZE]
        check = listOfNumber[i+SIZE]
        for j in range(SIZE-1):
            for k in range(j, SIZE):
                if (preamble[j] + preamble[k]) == check and not (preamble[j] == preamble[k]):
                    #print(f"{preamble[j]} + {preamble[k]} = {preamble[j] + preamble[k]}")
                    break
            else:
                continue
            break
        else: 
            return check
        
    
def part2(listOfNumber, check):
    for i in range(len(listOfNumber)):
        track = [listOfNumber[i]]
        j = i+1
        while sum(track) < check:
            track.append(listOfNumber[j])
            j+=1
        if sum(track) == check:
            out = min(track) + max(track)
            return out
    

main()
