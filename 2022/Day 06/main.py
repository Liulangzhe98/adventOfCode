# four characters that are all different.
def find_distinct_seq(buffer, size):
    seq = buffer[:size]
    for i, x in enumerate(buffer[size:], size):
        if len(set(seq)) == size:
            return i
        seq = seq[1:] + x

def part_one(file_path):
    with open(file_path, 'r') as file:
        return find_distinct_seq(file.readline(), 4)
    

def part_two(file_path):
    with open(file_path, 'r') as file:
        return find_distinct_seq(file.readline(), 14)

def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    
if __name__ == "__main__":
    main()
