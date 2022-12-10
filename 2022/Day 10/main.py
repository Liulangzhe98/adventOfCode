# Register x == 1

def part_one(file_path):
    instructions = []
    reg_x = 1
    sum_str = 0
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith("n"):
                instructions.append(None)
            else:
                num = int(line.split()[1])
                instructions.extend([None, num])
        for cyc, x in enumerate(instructions, 1):
            if cyc == 20 or cyc % 40 == 20:
                sum_str += cyc * reg_x
            if x != None:
                reg_x += x
    return sum_str


def part_two(file_path):
    instructions = []
    reg_x = 1
    CRT_STRING = "\n\t"
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith("n"):
                instructions.append(None)
            else:
                instructions.extend([None, int(line.split()[1])])   
        for cyc, x in enumerate(instructions, 0):
            if cyc % 40 == 0 and cyc > 1:
                CRT_STRING += "\n\t" 
            sprite = list(range(reg_x-1, reg_x+2))
            CRT_STRING += "#" if cyc % 40 in sprite else " "
            if x != None:
                reg_x += x
    return CRT_STRING

def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    
if __name__ == "__main__":
    main()
