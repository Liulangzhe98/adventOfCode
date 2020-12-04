import re

def main():
    file = open("input.txt", "r")
    
    valid = 0
    valid2 = 0
    
    passportList = []
    temp = []
    for line in file.readlines():
        if line == "\n":
            passportList.append(temp)
            temp = []
        else:
            temp.append(line.strip())
    # Otherwise you get a off by one
    if not temp in passportList:
        passportList.append(temp)
            
    for passport in passportList:
        newList = (" ".join(passport)).split(" ")
        
        if (len(newList) == 8) or 
        (len(newList) == 7 and not ("cid:" in str(newList))):
            valid += 1
            valid2 += checkValidity(newList)

        
    print(f"Amount of valid passports at 1: {valid}")
    print(f"Amount of valid passports at 2: {valid2}")
    
def checkValidity(passport):
    tempdict = {}
    # preparing the dictionary to check if all fields are in the within the ranges
    for item in passport:
        item = item.split(":")
        tempdict[item[0]] = item[1]
        
    if not '1920' <= tempdict['byr'] <= '2002':
        return 0
    if not '2010' <= tempdict['iyr'] <= '2020':
        return 0
    if not '2020' <= tempdict['eyr'] <= '2030':
        return 0
    if 'cm' in tempdict['hgt']:
        if not '150' <= tempdict['hgt'][:3] <= '193':
            return 0
    else:
        if not '59' < tempdict['hgt'][:2] <= '76':
            return 0
        
    if not (re.fullmatch(r'^#([a-f0-9]){6}$', tempdict['hcl'])):
        return 0
    if not tempdict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0
    if not (re.fullmatch(r'^[0-9]{9}$', tempdict['pid'])):
        return 0
    
        
    return 1
    


main()
