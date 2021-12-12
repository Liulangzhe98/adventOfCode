from collections import defaultdict

def DFS(graph, node, path):
    return [item for sublist in [path + ['end'] if next_node == 'end' else DFS(graph, next_node, path + [node]) for next_node in list(filter(lambda x: (x.islower() and x not in path) or x.isupper(), graph[node]))] for item in sublist]


def DFS2(graph, node, path, cvs):
    return [item for sublist in [path + ['end'] if next_node == 'end' else (([] if not cvs else DFS2(graph, next_node, path+[node], False)) if next_node.islower() and next_node in path else DFS2(graph, next_node, path+[node], cvs)) for next_node in list(filter(lambda x: x.isupper() or (x.islower() and x != 'start'), graph[node]))] for item in sublist]


def main():
    with open("input.txt") as file:
        input_list = [x.strip().split("-") for x in file.readlines()]
    cave_map = defaultdict(list)
    for key, val in input_list:
        cave_map[key].append(val)
        cave_map[val].append(key)

    print("(1) How many paths through this cave system are there that visit small caves at most once?")
    print(f"Answer: {sum(p.count('end') for p in [DFS(cave_map, next_node, ['start']) for next_node in cave_map['start']])}")

    print("(2) How many paths through this cave system are there?")
    print(f"Answer: {sum(p.count('end') for p in [DFS2(cave_map, next_node, ['start'], True) for next_node in cave_map['start']])}")


main()