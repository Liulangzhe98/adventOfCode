import re
from itertools import compress

class Board:
    def __init__(self, number_list):
        self.cells, self.marked = [int(x) for x in number_list], [True for _ in range(25)]
    
    def __str__(self):
        return f"Board: \n\t{self.cells}\n\t{self.marked}"

    def __repr__(self) -> str:
        return f"[\n {str(self)}\n]"

    def set_cell(self, number):
        try:
            self.marked[self.cells.index(number)] = False
        except:
            pass

    def bingo_check(self):
        return any(
            [not any(self.marked[i*5:(i+1)*5]) for i in range(5)]+
            [not any(self.marked[i::5]) for i in range(5)])

def part_one():
    drawing, bingo = init()
    for x in drawing:
        for b in bingo:
            b.set_cell(int(x))
            if b.bingo_check():
                print("(1) What will your final score be if you choose that board?")
                print(f"Answer: {sum(compress(b.cells, b.marked))*int(x)}")
                return


def part_two():
    drawing, bingo = init()
    for x in drawing:
        for b in bingo:
            b.set_cell(int(x))
        if len(bingo) == 1 and b.bingo_check():
            print("(2) Once it wins, what would its final score be?")
            print(f"Answer: {sum(compress(b.cells, b.marked))*int(x)}")
            return

        bingo = list(filter(lambda b: not b.bingo_check(), bingo))
       

def init():
    with open("input.txt") as file:
        input_list = file.read().split("\n\n")
    drawing_from =  re.findall("(\d+)", input_list[0])
    bingo = [Board(re.findall("(\d+)", x)) for x in input_list[1:]]
    return drawing_from, bingo


def main():
    part_one()
    part_two() 
 

main()