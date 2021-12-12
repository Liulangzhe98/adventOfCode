from collections import defaultdict
import re


def flatten(t):
    return [item for sublist in t for item in sublist]

def DFS (graph, node, path):
    if node == "end":
        return path + ['end']
    paths = [
        DFS(graph, next_node, path + [node])
        for next_node in list(filter(lambda x: 
        (x.islower() and x not in path) or x.isupper() , graph[node]))
    ]
    return flatten(paths)

def DFS2 (graph, node, path, cvs):
    if node == "end":
        return path + ['end']
    paths = []
    for next_node in list(filter(lambda x: x.isupper() , graph[node])):
        paths.append(DFS2(graph, next_node, path+[node], cvs))
    for next_node in list(filter(lambda x: x.islower() and x != 'start' , graph[node])):
        if next_node in path:
            if cvs:
                paths.append(DFS2(graph, next_node, path+[node], False))
        else: 
            paths.append(DFS2(graph, next_node, path+[node], cvs))
    return flatten(paths)


def part_one(init_vars):
    paths = []
    for next_node in init_vars['start']:
        paths.append(DFS(init_vars, next_node, ['start']))
    print("(1) How many paths through this cave system are there that visit small caves at most once?")
    print(f"Answer: {sum(p.count('end') for p in paths)}")



def part_two(init_vars):
    paths = []
    for next_node in init_vars['start']:
        paths.append(DFS2(init_vars, next_node, ['start'], True))
    print("(2) How many paths through this cave system are there?")
    print(f"Answer: {sum(p.count('end') for p in paths)}")
    

def main():
    with open("input.txt") as file:
        input_list = [re.match("(\w+)-(\w+)", x).groups() for x in file.readlines()]
    cave_map = defaultdict(list)
    for key, val in input_list:
        cave_map[key].append(val)
        cave_map[val].append(key)
    part_one(cave_map)
    part_two(cave_map)
    
main()
