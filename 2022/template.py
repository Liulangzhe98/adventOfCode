def part_one(file_path):
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            continue
    return None


def part_two(file_path):
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            continue
    return None

def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    
if __name__ == "__main__":
    main()
