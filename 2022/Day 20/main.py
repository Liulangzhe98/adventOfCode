from tqdm import tqdm

def sign(x):
    return -1 if x < 0 else 1

def get_value(moving):
    return [x[1] for x in moving]

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def filter_value( someList, value ):
    for x, y in someList:
        if y == value :
            return x,y


def part_one(file_path):
    with open(file_path, 'r') as file:
        org_array = [(e, int(x)) for e, x in enumerate(file.read().splitlines())]
        moving_list = org_array.copy()
        LEN_ARRAY = len(moving_list)

        # Loop over original array
        for pair in tqdm(org_array):
            movement = pair[1]

            if movement > 0:
                # Positive movement
                for _ in range(movement):
                    idx = moving_list.index(pair)
                    swapPositions(moving_list, idx, (idx+1)%LEN_ARRAY)
            else:
                for _ in range(abs(movement)):
                    idx = moving_list.index(pair)
                    if idx-1 < 0:
                        moving_list = moving_list[1:] + [moving_list[0]]
                        idx = moving_list.index(pair)
                    swapPositions(moving_list, idx, (idx-1)%LEN_ARRAY)
    result= filter_value( moving_list, 0 )
    idx_0 = moving_list.index(result)
    return sum([moving_list[(idx_0+x)%(LEN_ARRAY)][1] for x in [1000, 2000, 3000]])

def part_two(file_path):
    DECRYPTION_KEY = 811589153
    with open(file_path, 'r') as file:
        org_array = [(e, int(x)*DECRYPTION_KEY) for e, x in enumerate(file.read().splitlines())]
        moving_list = org_array.copy()
        LEN_ARRAY = len(moving_list)

        for round in range(10):
            # Loop over original array
            for pair in org_array:
                curr_idx = moving_list.index(pair)
                moving_list.remove(pair)

                new_idx = (curr_idx+pair[1])%len(moving_list)
                moving_list.insert(new_idx, pair)
       
    result= filter_value( moving_list, 0 )
    idx_0 = moving_list.index(result)
    return sum([moving_list[(idx_0+x)%(LEN_ARRAY)][1] for x in [1000, 2000, 3000]])


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt") # Takes 30+ minutes
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
