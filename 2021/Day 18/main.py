import re
import json
import math

def find_sub_list(sl,l):
    results=[]
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            results.append((ind,ind+sll-1))

    return results[0]


def part_one(input_list):
    result = input_list[0]
    for line in input_list[1:]:
        combined = f"[|{result}|,|{line}|]|"
        new_line = re.sub("(\d+|[\[\{\}\],])", "\g<1>|", reduce_snail(combined))
        while new_line != combined:
            combined = new_line
            new_line = re.sub("(\d+|[\[\{\}\],])", "\g<1>|", reduce_snail(combined))
        result = combined
    result = reduce_snail(result)
    print("(1) What is the magnitude of the final sum?")
    print(f"Answer: {calc_magnitude(result)}")


def part_two(input_list):
    homework_2 = 0
    for line in input_list:
        for line2 in input_list:
            if line == line2:
                continue
            combined = f"[|{line}|,|{line2}|]|"
            new_line = re.sub("(\d+|[\[\{\}\],])", "\g<1>|", reduce_snail(combined))
            while new_line != combined:
                combined = new_line
                new_line = re.sub("(\d+|[\[\{\}\],])", "\g<1>|", reduce_snail(combined))
            result = reduce_snail(combined)
            magni = calc_magnitude(result)
            homework_2 = max(homework_2, magni)
    print("(2) What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?")
    print(f"Answer: {homework_2}")

def reduce_snail(line):
    digits = list(map(int, re.findall("\d+", line)))
    digits_large = list(filter(lambda x: x>=10, (map(int, re.findall("\d+", line)))))
    new_str = ""
    can_do_action = True
    boundary = len(digits)
    depth = -1
    digits_read = []
    idx = 0
    for char in line.split("|"):
        if char == "[":
            depth += 1
            new_str += "["
        elif char == "]":
            if depth == 4 and can_do_action:
                left , right = idx-2, idx-1 
                if left != 0:
                    digits[left-1] = digits[left-1]+digits_read[-2]
                digits[left] = 0
                if right+1 == boundary:
                    digits.pop()
                else:
                    digits[right+1] = digits[right+1]+digits_read[-1]
                new_str = new_str[:new_str.rfind("{")-1]
                can_do_action = False
            new_str += "]"
            depth -= 1
        elif char.isnumeric():
            digits_read.append(int(char))
            new_str += f"{{{idx}}}"
            idx += 1
        else:
            new_str += char
    new_str = re.subn("\[({\d+})\]", "\g<1>", new_str)[0].format(*digits)
    # check if we need to split and only split most left
    if can_do_action and digits_large != []:
        d = digits_large[0]
        new = f"[{math.floor(d/2)},{math.ceil(d/2)}]"
        new_str = new_str.replace(str(d), new, 1)
        return new_str
    return new_str.format(*digits)


def calc_magnitude(snail):
    obj =  json.loads(snail)
    if isinstance(obj, int):
        return int(obj)
    return 3*calc_magnitude(json.dumps(obj[0]))+2*calc_magnitude(json.dumps(obj[1]))

def main():
    with open("input.txt") as file:
        input_list = [re.sub("(\d+|[\[\{\}\],])", "\g<1>|", x.strip()) for x in file.readlines()]
    part_one(input_list)
    part_two(input_list)


main()
