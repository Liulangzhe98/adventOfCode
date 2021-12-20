def enhance(matrix, algo, steps=2):
    EXTRA = 4*steps
    size = len(matrix[0])
    bigger = [['0']*(EXTRA+size) for _ in range(EXTRA)]
    for row in matrix:
        bigger.append(['0']*(EXTRA//2)+row+['0']*(EXTRA//2))
    bigger += [['0']*(EXTRA+size) for _ in range(EXTRA)]
    for i in range(steps):
        new_matrix = []
        for e, (a, b, c) in enumerate(zip(bigger, bigger[1:], bigger[2:]),1):
            new_row = []
            for col in range(1, len(a)-1):
                square = "".join(a[col-1:col+2]+b[col-1:col+2]+c[col-1:col+2])
                new_row.append(algo[int(square, 2)])
            new_matrix.append(new_row)
        bigger = new_matrix.copy()
    summed = 0
    for row in bigger:
        summed += row.count("1")
    return summed


def main():
    with open("input.txt") as file:
        algo, matrix  = file.read().replace("#", "1").replace(".","0").split("\n\n")
        algo = [str(x) for x in algo]
        matrix = [[str(x) for x in line] for line in matrix.split("\n")]

    print("(1) How many pixels are lit in the resulting image? (2 steps)")
    print(F"Answer: {enhance(matrix, algo)}")
    print("(2) How many pixels are lit in the resulting image? (50 steps)")
    print(f"Answer: {enhance(matrix, algo, 50)}")

            
main()
