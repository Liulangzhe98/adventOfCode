import re

def main():
    #415 -> a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b
    
    with open("input.txt", "r") as openobj:
        rules = []
        messages = []
        for line in openobj:
            line = line.strip().replace("\"", "")
            if re.match('^\d', line):
                    new = [line.split(": ")[0], line.split(": ")[1]]
                    rules.append(new)
            else:
                messages.append(line)
    rules = sorted(rules, key = lambda x: int(x[0]))
    headrule =  rules[0][1]
    print(f"Headrule : {headrule}")
        
    while re.search("\d", headrule):
    #for _ in range(15):
        newRule = ""
        for toReplace in headrule.split(" "):
            if toReplace.isdigit():
                replacement = rules[int(toReplace)][1]
                if "|" in replacement:
                    newRule += " ( "+replacement+" ) "
                else:
                    newRule += " " + replacement
            else:
                newRule += " " + toReplace
        headrule = newRule.strip()
    headrule = "^"+"".join(headrule.split(" "))
    headrule += "$"
    print(f"Final: {headrule}")
    count = 0
    for message in messages:
        if not re.search(headrule, message) == None:
            count += 1
        #print(f"M: {re.search(headrule, message)} | {message}")
    print(count)

main()
