import re

def main():
    #415 -> a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b
    
    #Hardcoded the changes into the input file
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
    
    rules = {rule[0] : rule[1] for rule in rules}
    print(rules)
    headrule =  rules['0']
    print(f"Headrule : {headrule}")
        
    while re.search("\d", headrule):
        newRule = ""
        for toReplace in headrule.split(" "):
            if toReplace.isdigit():
                replacement = rules[toReplace]
                if "|" in replacement:
                    newRule += " ( "+replacement+" ) "
                else:
                    newRule += " " + replacement
            else:
                newRule += " " + toReplace
        headrule = newRule.strip()
        print(f"Head: {headrule}")
    headrule = "^"+"".join(headrule.split(" "))
    headrule += "$"
    print(f"Final: {headrule}")
    count = 0
    for message in messages:
        if not re.search(headrule, message) == None:
            count += 1
    print(count)

main()
