def part_one(input_list):
    bits = [""]*len(input_list[0])
    for value in input_list:
        for c, bit in enumerate(value):
            bits[c] += bit
    print(bits)
    gamma = epsilon = ""
    for pos in bits:
        gamma += str(int(pos.count('1') > len(pos)/2))
        epsilon += str(int(pos.count('1') < len(pos)/2))
    print("(1) What is the power consumption of the submarine?")
    print(f"Answer: {int(gamma, 2)* int(epsilon, 2)}")

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
    pass

def main():
    with open("test.txt") as file:
        input_list = [x.strip()for x in file.readlines()]
    part_one(input_list)
    part_two(input_list)    


main()