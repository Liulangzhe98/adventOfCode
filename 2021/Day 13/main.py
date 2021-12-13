import re

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
   
    max_x = max(coords,key=lambda x: x[0])[0]
    max_y = max(coords,key=lambda x: x[1])[1] 
   
    paper = [[" " for _ in range(max_x+1)]  for _ in range(max_y+1)] 
    for x, y in coords:
        paper[y][x] = "#"
    
    for axis, fold_line in instructions:
        if axis == 'x':
            paper = [["#" if "#" in pair else " " for pair in zip(row, row[::-1])][:fold_line] for row in paper]
        else:
            paper = [paper[r1] if (r2 > max_y) else ['#' if '#' in x else ' ' for x in list(zip(paper[r1], paper[r2]))] for r1, r2 in zip(range(fold_line), range(fold_line*2, fold_line, -1) )]
    print("(2) What code do you use to activate the infrared thermal imaging camera system?")
    print_as_matrix(paper)
    

def main():
    with open("input.txt") as file:
        input_list = [x.strip() for x in file.readlines()]
    coords = [x.split(",") for x in filter(lambda x: not x.startswith("fold") and not x=="", input_list)]
    instructions = [re.search("fold along (x|y)=(\d+)",x).groups() for x in filter(lambda x: x.startswith("fold"), input_list)]
   
    part_one(coords, instructions)
    part_two(coords, instructions)
    
main()
