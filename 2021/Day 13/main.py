def print_as_matrix(matrix):
    print("[")
    for i in range(len(matrix)):
        print(f"  {''.join(matrix[i])}")
    print("]")

def part_one(coords, instructions):
    coords = [(int(a[0]), int(a[1])) for a in coords]
    instructions = [(a[0], int(a[1])) for a in instructions]
    
    max_x = max(coords,key=lambda x: x[0])[0]+1 #since counting from 0
    max_y = max(coords,key=lambda x: x[1])[1]+1 
    
    paper = [["." for _ in range(max_x)]  for _ in range(max_y)] 
    for x, y in coords:
        paper[y][x] = "#"
    for axis, coord in instructions:
        new_paper = []
        if axis == 'x':
            for row in paper:
                new_paper.append([ 
                    "#" if "#" in pair else "."
                    for pair in zip(row, row[::-1])
                ][:coord])
        else:
            for row in range(coord):
                new_paper.append([ 
                    "#" if "#" in pair else "."
                    for pair in zip(paper[row], paper[max_y-row-1])
                ])
        paper = new_paper.copy()
        break
    
    print("(1) How many dots are visible after completing just the first fold instruction on your transparent paper?")
    print(f"Answer: {sum([''.join(x).count('#') for x in paper])}")



def part_two(coords, instructions):
    coords = [(int(a[0]), int(a[1])) for a in coords]
    instructions = [(a[0], int(a[1])) for a in instructions]
    max_x, max_y = 0,0
    for axis, fold_line in instructions:
        new_coords = []
        print(f"Folding across {axis}={fold_line}")

    # coord = (x, y) coord[0] coord[1]

        if axis == 'x':
            for x, y in coords:
                if x > fold_line:
                    # print(x, y)
                    diff = x-fold_line
                    new_coords.append((x-2*diff, y))   
                else:
                    new_coords.append((x, y))     
            max_x = fold_line       
        else:
            for x, y in coords:
                if y > fold_line:
                    # print(x, y)
                    diff = y-fold_line
                    new_coords.append((x, y-2*diff))
                else:
                    new_coords.append((x, y))    
                max_y = fold_line  
        coords = list(set(new_coords.copy()))
        coords.sort()
        print(coords)
        print(len(coords))
    paper = [["." for _ in range(max_x)] for _ in range(max_y)]
    for x, y in coords:
        print(x, y, paper)
        paper[y][x] = "#"
    print_as_matrix(paper)
    
    pass
    # print("(2) What is the first step during which all octopuses flash?")
    # print(f"Answer: {step}")

import re

def main():
    with open("input.txt") as file:
        input_list = [x.strip() for x in file.readlines()]
    coords = [x.split(",") for x in filter(lambda x: not x.startswith("fold") and not x=="", input_list)]
    instructions = [re.search("fold along (x|y)=(\d+)",x).groups() for x in filter(lambda x: x.startswith("fold"), input_list)]
   
    part_one(coords, instructions)
    part_two(coords, instructions)
    
main()
