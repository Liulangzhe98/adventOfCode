def main():
    file = open('input.txt', 'r')
    
    maxID = 0
    listSeat = []
    
    for line in file.readlines():
        lowerRow, upperRow = (0,127)
        lowerSeat, upperSeat = (0,7)
        print(line.strip(), end = " | ")
        for char in line:
            rowDiff = (upperRow - lowerRow)//2
            seatDiff = (upperSeat - lowerSeat)//2
            if char == 'F':
                upperRow = lowerRow+rowDiff
            if char == 'B':
                lowerRow = lowerRow+rowDiff +1
            if char == 'L':
                upperSeat = lowerSeat+seatDiff
            if char == 'R':
                lowerSeat = lowerSeat+seatDiff+1
        seatID = lowerRow*8+lowerSeat
        listSeat.append(seatID)
        maxID = max(maxID, seatID)
        print(f"Row {lowerRow:3d} seat {lowerSeat} seat ID {seatID:3d} max {maxID}")
    
    print(f"The maxID is {maxID}")
    
    # part 2
    listSeat.sort()
    for count, ele in enumerate(listSeat, listSeat[0]):
        if not count == ele:
            break
    
    print(f"Your seat ID is: {count}")


main()
