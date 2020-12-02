import re


def main():
    file = open("input.txt", "r")

    total = 0

    for line in file.readlines():
        line = line.strip()
        policy = line.split(":")[0]
        password = line.split(":")[1].strip()
        listPos = re.findall('\d+', policy)
        start = int(listPos[0])
        end = int(listPos[1])
        char = policy.split()[1]

        a = password[start-1] == char
        b = password[end-1] == char
        test = (a and not b) or (not a and b)

        print(f"{start} | {char} | {end} => {password} = {test}")
        if test:
            total +=1

        # if (password.count(char) >= start and password.count(char) <= end):
        #     total +=1
    print(total)

main()