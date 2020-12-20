import time
import itertools
import re

def main(): 
    #part 1
    with open('input.txt') as openfileobject:
        som = 0
        for line in openfileobject:
            line = line.strip()
            while '(' in line:
                a = re.search('\(([^()]+)\)',line)
                if not a == None:
                    todo = a.group(1).split(" ")
                    while len(todo) >1:
                        if todo[1] == '+':
                            todo[0] = int(todo[0]) + int(todo[2])
                        if todo[1] == '*':
                            todo[0] = int(todo[0]) * int(todo[2])
                        todo.pop(1)
                        todo.pop(1)
                line = re.sub('\(([^()]+)\)', str(todo[0]), line, 1)
            todo = line.split(" ")
            while len(todo) > 1:
                if todo[1] == '+':
                    todo[0] = int(todo[0]) + int(todo[2])
                if todo[1] == '*':
                    todo[0] = int(todo[0]) * int(todo[2])
                todo.pop(1)
                todo.pop(1)
            som += todo[0]
        print(som)
            
    # part 2
    with open('input.txt') as openfileobject:
        som = 0
        for line in openfileobject:
            line = line.strip()
            while '(' in line:
                a = re.search('\(([^()]+)\)',line)
                if not a == None:
                    todo = a.group(1).split(" ")
                    while '+' in todo:
                        sign = todo.index('+')
                        todo[sign-1] = int(todo[sign-1]) + int(todo[sign+1])
                        todo.pop(sign)
                        todo.pop(sign)
                    while len(todo) > 1:
                        if todo[1] == '*':
                            todo[0] = int(todo[0]) * int(todo[2])
                        todo.pop(1)
                        todo.pop(1)
                line = re.sub('\(([^()]+)\)', str(todo[0]), line, 1)
            todo = line.split(" ")
            while '+' in todo:
                sign = todo.index('+')
                todo[sign-1] = int(todo[sign-1]) + int(todo[sign+1])
                todo.pop(sign)
                todo.pop(sign)
            while len(todo) > 1:
                if todo[1] == '*':
                    todo[0] = int(todo[0]) * int(todo[2])
                todo.pop(1)
                todo.pop(1)
            som += todo[0]
        print(som)
    
main()

