import math


def matrix_creation(text):
    matrix = [[int(x) for x in row] for row in text.splitlines()]
    return matrix, list(zip(*matrix))


def part_one(file_path):
    with open(file_path, 'r') as file:
        matrix, _ = matrix_creation(file.read())
        top = matrix[0]
        bottom = matrix[-1]
        coords = set()
        MAX = len(matrix)-1
        rules = [
            ("t[e]", "bounds[0]", "(i, e)"),
            ("t[MAX-e]", "bounds[1]", "(i, MAX-e)"),
            ("t[e]", "top[e]", "(i, e)"),
            ("b[e]", "bottom[e]", "(MAX-i, e)")
        ]

        for i in range(1, MAX):
            t, b = matrix[i], matrix[MAX-i]
            bounds = [t[0], t[-1]]

            for e in range(1, MAX):
                for x in rules:
                    if eval(f"{x[0]} > {x[1]}"):
                        coords.add(eval(x[2]))
                        exec(f"{x[1]} = {x[0]}")
    return len(coords) + len(top)*4-4


def count_vis(cons, trees):
    # stop at the first tree that is the same height or taller than
    # the tree under consideration.
    score = 0
    for x in trees:
        if x >= cons:
            return score + 1
        score += 1
    return score


def part_two(file_path):
    with open(file_path, 'r') as file:
        matrix, matrix_trans = matrix_creation(file.read())
        max_score = 0
        for i, row in enumerate(matrix):
            for e, cell in enumerate(row):
                # Look up, right, down, left
                temp_score = count_vis(cell, matrix_trans[e][:i][::-1]) * \
                    count_vis(cell, row[e+1:]) * \
                    count_vis(cell, matrix_trans[e][i+1:]) * \
                    count_vis(cell, row[:e][::-1])

                max_score = max(max_score, temp_score)
    return max_score


def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")


if __name__ == "__main__":
    main()
