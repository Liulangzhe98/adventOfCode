import re


def main():
    file = open("input.txt", "r")

    total_1 = 0
    total_2 = 0

    for line in file.readlines():
        line = line.strip()
        policy = line.split(":")[0]
        password = line.split(":")[1].strip()
        listPos = re.findall('\d+', policy)
        start = int(listPos[0])
        end = int(listPos[1])
        char = policy.split()[1]

        a = password[start - 1] == char
        b = password[end - 1] == char
        test = (a and not b) or (not a and b)

        if start <= password.count(char) <= end:
            total_1 += 1
        if test:
            total_2 += 1

    print(f"Total amount of right passwords at puzzle 1: {total_1}")
    print(f"Total amount of right passwords at puzzle 2: {total_2}")


main()
