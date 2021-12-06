import re
from itertools import compress

def print_field(max_x, max_y, field):
    print(field)
    print("[")
    print(max_x)
    end_col = max_y+1
    for i in range(end_col):
        row = field[i*end_col:(i+1)*end_col]
        print(f"  {row}")
    print("]")

def print_fieldB(field):
    print("[")
    for row in field:
        print(f"  {row}")
    print("]")

def part_one(input_list, max_x, max_y):
    field_b = [ [0]*(max_x+1) for _ in range(max_y+1) ]
    for c1, c2 in input_list:
        x1, y1, x2, y2 = *c1, *c2
        if x1 != x2 and y1 != y2:
            continue     
        fill_row = list(range(x1, x2+1))
        fill_col = list(range(y1, y2+1))
        if len(fill_col) == 1: # Horizontal line
            row = fill_col[0]
            for idx in fill_row:
                field_b[row][idx] += 1
        else:
            col = fill_row[0]
            for idx in fill_col:
                field_b[idx][col] += 1
    b = [x for row in field_b for x in row if x >= 2]
    print(len(b))


def part_two(input_list, max_x, max_y):
    field_b = [ [0]*(max_x+1) for _ in range(max_y+1) ]
    for c1, c2 in input_list:
        x1, y1, x2, y2 = *c1, *c2
        if (x1-x2 == y1-y2):
            diff = abs(x1-x2)
            to_do = [ 
                (c1[0]+i, c1[1]+i)
                for i in range(diff+1)
            ]
            print(to_do)
            for x, y in to_do:
                field_b[y][x] += 1
            continue
        if (abs(x1-x2) == abs(y1-y2)):
            diff = abs(x1-x2)
            to_do = [ 
                (c1[0]+i, c1[1]-i)
                for i in range(diff+1)
            ]
            for x, y in to_do:
                field_b[y][x] += 1
            continue
        fill_row = list(range(x1, x2+1))
        fill_col = list(range(y1, y2+1))
        if len(fill_col) == 1: # Horizontal line
            row = fill_col[0]
            for idx in fill_row:
                field_b[row][idx] += 1
        else:
            col = fill_row[0]
            for idx in fill_col:
                field_b[idx][col] += 1
    b = [x for row in field_b for x in row if x >= 2]
    print(len(b))
    
def init():
    with open("input.txt") as file:
        input_list = re.findall(
            "(\d+,\d+) -> (\d+,\d+)", 
            " ".join([x.strip()for x in file.readlines()]))
        input_list = [ 
            sorted(
                [tuple([int(b) for b in begin.split(",")]), 
                 tuple([int(b) for b in end.split(",")])]
                , key= lambda x: (x[0], x[1])
            )
            for begin, end in input_list
        ]
        input_list = sorted(input_list, key=lambda x: x[0][1] == x[1][1], reverse=True)
        print(input_list)
        max_y = max(input_list, key=lambda x: x[1][1])[1][1]
        max_x = max(input_list, key=lambda x: x[1][0])[1][0]
    return input_list, max_x, max_y


def main():
    # (col, row) -> (col, row)
    init_vars = init()
    part_one(*init_vars)
    part_two(*init_vars) 
 

main()