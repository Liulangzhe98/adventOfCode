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
    
    rules = {rule[0] : rule[1] for rule in rules}
    print(rules)
    headrule =  rules['0']
    print(f"Headrule : {headrule}")
        
    while re.search("\d", headrule):
    #for _ in range(2):
        newRule = ""
        for toReplace in headrule.split(" "):
            if toReplace.isdigit():
                replacement = rules[toReplace]
                #if toReplace in replacement: # special inf loop protection
                    #a = [x for x in replacement.split(" | ") if toReplace not in x]
                    #if toReplace == '8':
                        #newRule += " ( "  + "".join(a) + " )+ "
                    #else:
                        #rule_11 = ""
                        #for x in range(1,5):
                            #options = "".join(a).split(" ")
                            #rule_11 += f"( ({options[0]} ){{{x}}}({options[1]} ){{{x}}} )"
                        #print(rule_11)
                    
                #else:
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
        #print(f"M: {re.search(headrule, message)} | {message}")
    print(count)

main()
