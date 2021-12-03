def part_one(input_list):
    bits = [""]*len(input_list[0])
    for value in input_list:
        for c, bit in enumerate(value):
            bits[c] += bit
    gamma = epsilon = ""
    for pos in bits:
        gamma += str(int(pos.count('1') > len(pos)/2))
        epsilon += str(int(pos.count('1') < len(pos)/2))
    print("(1) What is the power consumption of the submarine?")
    print(f"Answer: {int(gamma, 2)* int(epsilon, 2)}")

def part_one_one_liner(input_list):
    gamma = eps = ""
    bit = 0
    [(bit:= int(x.count('1') > len(x)/2), gamma:= gamma + str(bit), eps:= eps + str(1-bit))   for x in [ "".join([value[i] for value in input_list]) for i in range(len(input_list[0]))]]
    print("(1) What is the power consumption of the submarine?")
    print(f"Answer: {int(gamma, 2)* int(eps, 2)}")

def part_two(input_list):
    oxygen_gen = input_list.copy() # most common
    for i in range(len(oxygen_gen[0])):
        if(len(oxygen_gen) == 1):
            continue
        bits = ""
        for value in oxygen_gen:
            bits += value[i]
        pref_bit = str(int(bits.count('1') >= len(bits)/2))
        oxygen_gen = list(filter(lambda x: x[i] == pref_bit, oxygen_gen))
    oxygen_scrub = input_list.copy() # least common
    for i in range(len(oxygen_scrub[0])):
        if(len(oxygen_scrub) == 1):
            continue
        bits = ""
        for value in oxygen_scrub:
            bits += value[i]
        pref_bit = str(int(bits.count('1') < len(bits)/2))
        oxygen_scrub = list(filter(lambda x: x[i] == pref_bit, oxygen_scrub))
    print("(2) What is the life support rating of the submarine?")
    print(f"Answer: {int(oxygen_gen[0], 2)* int(oxygen_scrub[0], 2)}")

def part_two_one_liner(input_list):
    a = sorted(input_list)
    ox, carb = a, a
    [(
        bit := ox[len(ox)//2][i], 
        ox := [v for v in ox if len(ox) == 1 or v[i] == bit],
        bit := carb[len(carb)//2][i],
        carb := [v for v in carb if len(carb) == 1 or v[i] != bit]
    ) for i in range(len(a[0]))]

    print("(2) What is the life support rating of the submarine?")
    print(f"Answer: {int(ox[0], 2)* int(carb[0], 2)}")


def main():
    with open("input.txt") as file:
        input_list = [x.strip()for x in file.readlines()]
    part_one(input_list)
    part_two(input_list) 
    print(" === one liners === ")
    part_one_one_liner(input_list)
    part_two_one_liner(input_list)
    

main()