import string

def part_one(template, pair_insertions):
    for _ in range(1, 11):
        pairs = zip(template, template[1:])
        template = ""
        for pair in pairs:
            template += pair[0] + pair_insertions[''.join(pair)]
        template += pair[1]
    b = sorted([template.count(x) for x in string.ascii_uppercase if template.count(x) > 0])
    print("(1) What do you get if you take the quantity of the most common element and subtract the quantity of the least common element for 10 steps?")
    print(f"Answer: {b[-1]-b[0]}")
  

def part_two(template, pair_insertions):
    pairs = [f"{a}{b}" for a,b in zip(template, template[1:])]
    h_d = create_huge_dict(pair_insertions, 40, sorted(set(pair_insertions.values())))

    depth = 40 - 1
    unique_vals = sorted(set(pair_insertions.values()))
    result = [0 for _ in range(len(unique_vals))]
    offset = [0 for _ in range(len(unique_vals))]
    for p in pairs:
        result = [a+b for a, b in zip(result, h_d[depth][p])]
        offset[unique_vals.index(p[1])] += 1
    offset[unique_vals.index(p[1])] -= 1
    result = [a-b for a,b in zip(result, offset)]
    result.sort()
    
    print("(2) What do you get if you take the quantity of the most common element and subtract the quantity of the least common element for 40 steps?")
    print(f"Answer: {result[-1]-result[0]}")
    
def create_huge_dict(pairs, depth, unique_values):
    output = dict([(x, {}) for x in range(depth+1)])
    for k, v in pairs.items():
        me = k[0]+v+k[1]
        output[0][k] = [me.count(x) for x in unique_values]
    for i in range(1, depth+1):
        for k, v in pairs.items():
            LHS = output[i-1][k[0]+v]
            RHS = output[i-1][v+k[1]]
            sum_list = [a+b for a, b in zip(LHS, RHS)]
            sum_list[unique_values.index(v)] -= 1
            output[i][k] = sum_list
    return output


def main():
    with open("input.txt") as file:
        template = file.readline().strip()
        input_list = dict([x.strip().split(" -> ") for x in file.readlines()][1:])

    part_one(template, input_list)
    part_two(template, input_list)
    
main()
