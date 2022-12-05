import re 

def my_replace(in_str):
    return re.sub("\[|\]", " ", in_str)

def parse_content(content):
    start, instructions = content.split("\n\n")
    crates = start.split("\n")[:-1]
    first_row = my_replace(crates[0])[1::4]
    pillars = {i: "" for i in range(1, 1+len(first_row))}
    for line in crates[::-1]:
        for i, x in enumerate(my_replace(line)[1::4], 1):
            #"|[D] |[C] | " This is an example line split into the chunks of 4 
            #   and the selecting the character from that chunk
            if x != " ":
                pillars[i] += x
    return pillars, instructions

def eval_instr(pillars, instructions, grab_all=False):
    for line in instructions.splitlines():
        values = re.match("move (\d+) from (\d+) to (\d+)", line).groups()

        amount, start, end = [int(x) for x in values]
        temp = pillars[start][-amount:][::(0-(1-2*grab_all))]
        pillars[start] = pillars[start][:-amount]
        pillars[end] += temp


def part_one(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        pillars, instructions = parse_content(content)
        eval_instr(pillars, instructions)
    return "".join([x[-1] for x in pillars.values()])


def part_two(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        pillars, instructions = parse_content(content)
        eval_instr(pillars, instructions, grab_all=True)
    return "".join([x[-1] for x in pillars.values()])

def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    
if __name__ == "__main__":
    main()
