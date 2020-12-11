import time

def main():
    start = time.time()
    f = open("input.txt", "r")
    f = open("test.txt", "r")
    chairs = []
    for line in f.readlines():
        line = line.strip()
        row = []
        
        #floor is 0, seat is 1, occupied is 2
        for char in line:
            if char == '.':
                row.append(0)
            if char == 'L':
                row.append(1)
            if char == '#':
                row.append(2)
        chairs.append(row)
   
    print(f"Reading took: {(time.time()-start)*1000:.2f}ms")
   
    start = time.time()
    part1Answer = part1(chairs)
    print(f"Part 1 is : {part1Answer} {(time.time()-start)*1000:.2f}ms")
    start = time.time()
    part2Answer = part2(chairs)
    print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms")
    
    # == Works on the smaller set, however it doesnt on the larger set
    #start = time.time()
    #part2AnswerWithLambda = part2Lambda(chairs)
    #print(f"Part 2 (lambda) is : {part2AnswerWithLambda} {(time.time()-start)*1000:.2f}ms")
    
    
def part2Lambda(chairs):
    prev = 0
    # direction topleft, top, top right, left, right, bot left, bot, bot right
    options = [
        lambda row, col, i: (row-i, col-i)  ,
        lambda row, col, i: (row-i, col)        ,
        lambda row, col, i: (row-i, col+i) ,
        lambda row, col, i: (row, col-i)       ,
        lambda row, col, i: (row, col+i)      ,
        lambda row, col, i: (row+i, col-i)  ,
        lambda row, col, i: (row+i, col)        ,
        lambda row, col, i: (row+i, col+i) 
    ]
    
    while(True):
        copyChairs = []
        for cnt, row in enumerate(chairs):
            copyRow = [] 
            for cnt2, chair in enumerate(row):
                if chair == 0:
                    copyRow.append(0)
                else: 
                    ignoreMe = [False]*8
                    occu = 0
                    maxSteps = max(len(row)-1, len(chairs))
                    for i in range(1, maxSteps):
                        for DIR in range(0,8):
                            if ignoreMe[DIR]:
                                continue
                            (row2, col) = options[DIR] (cnt, cnt2, i)
                            #print(f"{row2} {col} | {maxSteps} {len(chairs)} {len(row)}")
                            if not ignoreMe[DIR] and min(row2,col)>=0 and max(row2, col) < maxSteps:
                                value = chairs[row2][col] 
                                if value == 2:
                                    occu += 1
                                if not value == 0:
                                    ignoreMe[DIR] = True
                            else:
                                ignoreMe[DIR] = True
                    if (chair == 1 and occu == 0):
                        copyRow.append(2)
                    elif (chair == 2 and occu >= 5):
                        copyRow.append(1)
                    else:
                        copyRow.append(chair)
            copyChairs.append(copyRow)
        total = sum([i.count(2) for i in copyChairs])
        chairs = copyChairs.copy()
        print(total)
        if total == prev:
            break
        else:
            prev = total
    return prev
    
    
def part2(chairs):
    prev = 0
    while(True):
        copyChairs = []
        for cnt, row in enumerate(chairs):
            copyRow = [] 
            occurs = []
            for cnt2, chair in enumerate(row):
                occu = 0
            #check row 
                #left side of chair
                for i in range(cnt2-1, -1,-1):
                    if chairs[cnt][i] == 1:
                        break                    
                    if chairs[cnt][i] == 2:
                        occu += 1
                        break
                #righht side of chair
                for i in range(cnt2+1, len(row)):
                    if chairs[cnt][i] == 1:
                        break    
                    if chairs[cnt][i] == 2:
                        occu += 1
                        break
            #check column
                #top side of chair
                for i in range(cnt-1, -1,-1):
                    if chairs[i][cnt2] == 1:
                        break    
                    if chairs[i][cnt2] == 2:
                        occu += 1
                        break
                #bottom side of chair
                for i in range(cnt+1, len(chairs)):
                    if chairs[i][cnt2] == 1:
                        break    
                    if chairs[i][cnt2] == 2:
                        occu += 1
                        break
            #check diagonals
                #top left - chair diagonal
                maxSteps = min(cnt, cnt2)
                for i in range(1, maxSteps+1):
                    if chairs[cnt-i][cnt2-i] == 1:
                        break
                    if chairs[cnt-i][cnt2-i] == 2:
                        occu += 1
                        break
                #chair - bot right diagonal
                maxSteps = min(len(chairs)-cnt, len(row)-cnt2)
                for i in range(1, maxSteps):
                    if chairs[cnt+i][cnt2+i] == 1:
                        break
                    if chairs[cnt+i][cnt2+i] == 2:
                        occu += 1
                        break
                #top right - chair diagonal
                maxSteps = min(cnt, len(row)-1-cnt2)
                for i in range(1, maxSteps+1):
                    if chairs[cnt-i][cnt2+i] == 1:
                        break
                    if chairs[cnt-i][cnt2+i] == 2:
                        occu += 1
                        break
                #chair - bot left diagonal
                maxSteps = min(len(chairs)-1-cnt, cnt2)
                for i in range(1, maxSteps+1):
                    if chairs[cnt+i][cnt2-i] == 1:
                        break
                    if chairs[cnt+i][cnt2-i] == 2:
                        occu += 1
                        break
                if (chair == 1 and occu == 0):
                    copyRow.append(2)
                elif (chair == 2 and occu >= 5):
                    copyRow.append(1)
                else:
                    copyRow.append(chair)
                occurs.append(occu)
            copyChairs.append(copyRow)
        total = sum([i.count(2) for i in copyChairs])
        chairs = copyChairs.copy()
        if total == prev:
            break
        else:
            prev = total
            
    return prev

def part1(chairs):
    prev = 0
    while(True):
        copyChairs = []
        for cnt, row in enumerate(chairs):
            copyRow = []            
            for cnt2, chair in enumerate(row):
                occu = 0
                right = min(len(row), cnt2+1)+1
                left = max(0, cnt2-1)
                if cnt >= 1:
                    occu += chairs[cnt-1][left:right].count(2)
                if cnt2 >= 1:
                    occu += (chairs[cnt][cnt2-1] == 2)
                if cnt2 < len(row) -1:
                    occu += (chairs[cnt][cnt2+1] == 2)
                if cnt < len(chairs) -1:
                    occu += chairs[cnt+1][left:right].count(2)
                if (chair == 1 and occu == 0):
                    copyRow.append(2)
                elif (chair == 2 and occu >= 4):
                    copyRow.append(1)
                else:
                    copyRow.append(chair)
            copyChairs.append(copyRow)
            for x in copyRow:
                seat = [".","L","#"]
        total = sum([i.count(2) for i in copyChairs])
        chairs = copyChairs.copy()
        if total == prev:
            break
        else:
            prev = total
            
    return prev

main()
