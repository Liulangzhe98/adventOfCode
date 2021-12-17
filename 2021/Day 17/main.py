import re
import math

def part_one(input_list):
    target_x = (int(input_list[0][0]), int(input_list[0][1]))
    target_y = (int(input_list[0][2]), int(input_list[0][3]))

    x_possible = [ (i, [max(0, i-j) for j in range(10)]) for i in range(10)]
    for i in range(1, target_x[1]):
        x_possible = (i, sum(range(i+1)))
        if x_possible[1] >= target_x[0]:
            break
    least_steps = x_possible[0]

    #determine y
    max_coord = (0,0)
    for y in range(least_steps, 100):
        step = least_steps
        while True:
            my_sum = 0
            tracker = []
            for i in range(y, y-step, -1):
                my_sum += i
                tracker.append(my_sum)
            if my_sum < target_y[0]:
                break
            if my_sum <= target_y[1]:
                max_coord = max(max_coord, (y, max(tracker)), key=lambda x: x[1])
                print(tracker)
            
                break
            step += 1
    print("(1) What is the highest y position it reaches on this trajectory?")
    print(f"Answer: {max_coord[1]}")

def part_two(input_list):
    target_x = (int(input_list[0][0]), int(input_list[0][1]))
    target_y = (int(input_list[0][2]), int(input_list[0][3]))

    elevation = list(range(target_y[0], abs(target_y[0])))
    print(elevation)
    steps_possible = []
    for ele in elevation:
        b = []
        i = ele
        my_sum = 0
        while True:
            b.append(my_sum)
            my_sum += i
            i -= 1
            if my_sum <= target_y[0]:
                break

        steps_possible.append((ele, b))
    for start_y in steps_possible:
        print(f"start Y: {start_y}")
    print("==================")

    total = 0
    max_steps = 0
    for idx in range(1, target_x[1]+1):
        print(f"Checking{idx}")
        
        for start_y in steps_possible:
            coord = (0,0)
            dx, dy = idx, start_y[0]
            # print(f"DX, DY = {dx} {dy}")
            
            while True: # do step
                coord = (coord[0]+dx, coord[1]+dy)
                dx = max(0, dx-1)
                dy -= 1
                if target_x[0] <= coord[0] <= target_x[1] and target_y[0] <= coord[1] <= target_y[1]:
                    total += 1
                    break


                if coord[1] <= target_y[0] or coord[0] > target_x[1]:
                    break
            # print(coord)
            # check if coord is inside
            
        # exit()
    print(total)



def main():
    with open("input.txt") as file:
        input_list = re.findall("x=(-?\d+)..(\-?\d+), y=(-?\d+)..(\-?\d+)", file.readline())
    part_one(input_list)
    part_two(input_list)



    # input_list[0] = "0"*((4-len(input_list[0])%4)%4) + input_list[0]
    # packet, _ = decode_BITS(input_list[0], 0)
    # print("(1) What do you get if you add up the version numbers in all packets?")
    # print(f"Answer: {packet['v']}")
    # print("(2) What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?")
    # print(f"Answer: {packet_to_number(packet)}")


main()
