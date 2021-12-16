import math

def decode_BITS(bin_str, indent, pos=0):
    if len(bin_str)< 11:
        return None, 0, 0

    packet = {"v": int(bin_str[pos:pos+3],2), "t": int(bin_str[pos+3:pos+6],2)}
    pointer = pos+6

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
        values = []
        if i == '0': # 15-bit number representing the number of bits for the packages 
            length = int(bin_str[pointer:pointer+15],2)
            pointer += 15
            end = pointer+length
            while pointer != end:
                packet_back, pointer = decode_BITS(bin_str, indent+1, pos=pointer)
                packet["v"] += packet_back['v']
                values.append(packet_back)
        else: # 11-bit number representing the number of sub-packets
            amount = int(bin_str[pointer:pointer+11],2)
            pointer += 11
            for _ in range(amount):
                packet_back, pointer = decode_BITS(bin_str, indent+1, pointer)
                packet["v"] += packet_back['v']
                values.append(packet_back)
        packet['val'] = values.copy()
    return packet, pointer

eval_dict = [sum, math.prod, min, max, None, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]]


def packet_to_number(packet):
    if packet['t'] == 4:
        return packet['val']
    return eval_dict[packet['t']]([packet_to_number(p) for p in packet['val']])


def main():
    with open("input.txt") as file:
        input_list = [f"{int(x.strip(), 16):b}" for x in file.readlines()]
    input_list[0] = "0"*((4-len(input_list[0])%4)%4) + input_list[0]
    packet, _ = decode_BITS(input_list[0], 0)
    print("(1) What do you get if you add up the version numbers in all packets?")
    print(f"Answer: {packet['v']}")
    print("(2) What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?")
    print(f"Answer: {packet_to_number(packet)}")


main()
