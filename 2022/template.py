def part_one(file_path):
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            continue
    return None


def part_two(file_path):
    with open(file_path, 'r') as file:
        ffor line in file.read().splitlines():
            continue
    return None

def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    
if __name__ == "__main__":
    main()
