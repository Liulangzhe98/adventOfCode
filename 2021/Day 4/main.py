import re

class Board:
    def __init__(self, number_list):
        self.cells, self.marked = self.create_cells(number_list)
    
    def __str__(self):
        return f"Board: \n\t{self.cells}\n\t{self.marked}"

    def __repr__(self) -> str:
        return f"[\n {str(self)}\n]"

    def create_cells(self, number_list):
        output = []
        for x in number_list:
            output.append(int(x))
    
        return output, [False for i in range(25)]

    def set_cell(self, number):
        try:
            idx = self.cells.index(number)
            self.marked[idx] = True
            return 1
        except:
            return 0

    def bingo_check(self):
        rows = [all(self.marked[i*5:(i+1)*5]) for i in range(5)]
        cols = [all(self.marked[i::5]) for i in range(5)]
        return any(rows+cols)

def part_one():
    drawing, bingo = init()
    for x in drawing:
        for b in bingo:
            b.set_cell(int(x))
            if b.bingo_check():
                sum_list = [k
                    for k, v in list(zip(b.cells, b.marked)) if v == False
                ]
                print("(1) What will your final score be if you choose that board?")
                print(f"Answer: {sum(sum_list)*int(x)}")
                return

def part_two():
    drawing, bingo = init()
    for x in drawing:
        for b in bingo:
            b.set_cell(int(x))
        if len(bingo) == 1 and b.bingo_check():
            sum_list = [k
                for k, v in list(zip(b.cells, b.marked)) if v == False
            ]
            print("(2) Once it wins, what would its final score be?")
            print(f"Answer: {sum(sum_list)*int(x)}")
            return

        bingo = list(filter(lambda b: not b.bingo_check(), bingo))
       

def init():
    with open("input.txt") as file:
        input_list = [x.strip() for x in file.readlines()]
    drawing_from =  re.findall("(\d+)", input_list[0])
    board_amount = len(list(filter(lambda x: x != "", input_list)))//5
    bingo = []
    for i in range(board_amount):
        board_str = ""
        for j in range(5):
            board_str += f"{input_list[2+i*6+j]} "
        numbers = re.findall("(\d+)", board_str)
        bingo.append(Board(numbers))
    return drawing_from, bingo


def main():
    part_one()
    part_two() 

    

main()