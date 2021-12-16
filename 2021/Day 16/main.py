def print_with(str, indent=0):
    print("  "*indent+str)


import time

def decode_BITS(bin_str, indent, pos=0):
    # print(f"Full: {bin_str}")
    
    if len(bin_str)< 11:
        return None, 0, 0

    packet = {
        "v": int(bin_str[pos:pos+3],2), "t": int(bin_str[pos+3:pos+6],2)
    }
    
    pointer = pos+6

    # print(f"From: {bin_str[pointer:]:>{len(bin_str)}}")

    if packet["t"] == 4:
        number = ""
        while bin_str[pointer] == '1':
            number += bin_str[pointer+1:pointer+5]
            pointer += 5
        number += bin_str[pointer+1:pointer+5]
        pointer += 5
        packet['val'] = int(number,2)
    else:
        i = bin_str[pointer]
        pointer += 1
        # print_with(f"I = {i}", indent)
        values = []
        if i == '0': # 15-bit number representing the number of bits for the packages 
            length = int(bin_str[pointer:pointer+15],2)
            pointer += 15
            end = pointer+length
            # print(F"End should be at {pointer+length}")
            # print_with(f"Number of bits for the next packages: {length}", indent)
            while pointer != end:
                p_back, pointer = decode_BITS(bin_str, indent+1, pos=pointer)
                packet["v"] += p_back['v']
                values.append(p_back)
            # print_with(f"== End of I = 0",indent)
        else: # 11-bit number representing the number of sub-packets
            amount = int(bin_str[pointer:pointer+11],2)
            pointer += 11
            # print_with(f"Number of packages: {amount}", indent)
            for idx in range(amount):
                p_back, pointer = decode_BITS(bin_str, indent+1, pointer)
                packet["v"] += p_back['v']
                # print_with(f"Package[{idx}] = {p_back}", indent)
                values.append(p_back)
            # print_with(f"== End of I = 1", indent)
        packet['val'] = values.copy()
    # print_with(f"{bin_str[pos:pointer]} return {packet}, {pointer}", indent)
    return packet, pointer

def packet_to_number(packet):
    if packet['t'] == 0:
        return sum([ 
            packet_to_number(p)
            for p in packet['val']
        ])
    elif packet['t'] == 1:
        product = 1
        for p in packet['val']:
            product *= packet_to_number(p)
        return product
    elif packet['t'] == 2:
        return min([ 
            packet_to_number(p)
            for p in packet['val']
        ])
    elif packet['t'] == 3:
        return max([ 
            packet_to_number(p)
            for p in packet['val']
        ])
    elif packet['t'] == 4:
        return packet['val']
    elif packet['t'] == 5:
        return int(packet_to_number(packet['val'][0]) > packet_to_number(packet['val'][1]))
    elif packet['t'] == 6:
        return int(packet_to_number(packet['val'][0]) < packet_to_number(packet['val'][1]))
    elif packet['t'] == 7:
        return int(packet_to_number(packet['val'][0]) == packet_to_number(packet['val'][1]))


def main():
    with open("input.txt") as file:
        input_list = [f"{int(x.strip(), 16):b}" for x in file.readlines()]
    for i in range(len(input_list)):
        print((4-len(input_list[i])%4)%4)
        input_list[i] = "0"*((4-len(input_list[i])%4)%4) + input_list[i]
    for i in range(len(input_list)):
        packet, _ = decode_BITS(input_list[i], 0)

        print(f"Decoded: {packet['v']} {packet['t']} => {packet_to_number(packet)}")
    # print("(1) What is the lowest total risk of any path from the top left to the bottom right?")
    # print(f"Answer: {solve(*graph_maker(input_list)).get_dist()}")
    # print("(2) What is the lowest total risk of any path from the top left to the bottom right?")
    # print(f"Answer: {solve(*graph_maker(input_list,5)).get_dist()}")


main()
