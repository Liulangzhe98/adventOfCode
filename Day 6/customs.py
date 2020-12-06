# Added one newline after the input, so the adding of groups doesn't need extra cases
import string

def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    
    groups = []
    group = []
    for item in lines:
        if item == '':
            groups.append(group)
            group = []
        else: 
            group.append(item)
            
    count = 0
    countAll = 0
            
    for group in groups:
        for x in string.ascii_lowercase:
            count += any((x in word) for word in group)
            countAll += all((x in word) for word in group)

    print(f"The sum of questions anyone in the group answered yes: {count}")
    print(f"The sum of questions everyone in the group answered yes: {countAll}")



main()
