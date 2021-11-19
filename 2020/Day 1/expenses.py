def main():
    file = open("input.txt", "r")

    expenses = []

    for line in file.readlines():
        line = line.strip()
        expenses.append(int(line))

    for x in expenses:
        for y in expenses:
            if x + y == 2020:
                print(x * y)
            for z in expenses:
                if x + y + z == 2020:
                    print(x * y * z)


main()
