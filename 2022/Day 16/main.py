import re 
import json
import math

class Valve(object):
    """docstring for Valve"""
    def __init__(self, name, flow, connected):
        super(Valve, self).__init__()
        self.name = name
        self.flow = flow
        self.connected = connected
        self.open = False

    def __str__(self):
        return f"[{self.name}] : Flow: {self.flow} | connected: {self.connected}"
        
    def __repr__(self):
        return str(self)


class Person(object):
    """docstring for Person"""
    def __init__(self, name, at='AA', next_move=0, release=0):
        super(Person, self).__init__()
        self.name = name
        self.at = at
        self.next_move = next_move
        self.release = release
        
    def __str__(self):
        return f"{(self.next_move, self.name, self.at)}"

    def __repr__(self):
        return str(self)


def parser(line):
    name, flow = re.findall("([A-Z]{2}).*=(\d+)", line)[0]
    connections = line.split(";")[1].split(" ")[5:]
    connections = list(map(lambda s: s.replace(",", ""), connections))
    return (name, Valve(name, int(flow), connections), connections)


def floyd(num_vert, list_edges, labels):
    # From wikipedia
    dist = [[math.inf for _ in range(num_vert)] for _ in range(num_vert)]

    for (begin, end) in list_edges:
        idx, idx1 = (labels.index(begin), labels.index(end))
        dist[idx][idx1] = 1
    for i in range(num_vert):
        dist[i][i] = 0
    for k in range(num_vert):
        for i in range(num_vert):
            for j in range(num_vert):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def solve(graph, dist_matrix, POI, labels, results, time_left=30, coord='AA', pressure_total=0, visited=set(), path=[]):
    at, at_idx = graph[coord], labels.index(coord)
    best_option = []

    if not POI.difference(visited) or time_left <= 0:
        results.append((pressure_total, path))
        return True

    for p in list(filter(lambda x: x not in visited, POI)):
        idx = labels.index(p)
        time_spent = dist_matrix[at_idx][idx] + 1
        if (time_left - time_spent) >= 0:
            pressure = graph[p].flow*(time_left-time_spent)
            best_option.append((p, pressure, time_spent))

    for option in sorted(best_option, key=lambda x: x[1], reverse=True):
        v = visited.copy()
        v.add(option[0])
        res = solve(graph, dist_matrix, POI, labels, results, time_left-option[2], option[0], pressure_total+option[1],v, path+[option[0]])
    return True


def get_options(graph, dist_matrix, labels, pos, POI, time_left):
    pos = labels.index(pos)
    best_option = []
    for (p, _) in list(POI):
        idx = labels.index(p)
        time_spent = dist_matrix[pos][idx] + 1
        if (time_left - time_spent) > 0:
            flow = graph[p].flow
            pressure = flow*(time_left-time_spent)
            # print(f"{coord} => {p} == {pressure}")
            best_option.append((p, pressure, flow, time_spent))
    return sorted(best_option, key=lambda x: x[1], reverse=True)


def solve_iter(graph, dist_matrix, POI, labels, results, queue, path=[],
    time_max = 26):
    (time_curr, person) = queue.pop(0)
    options = get_options(graph, dist_matrix, labels, person[1], POI, time_max-time_curr)

    for (p, f) in [(x[0], x[2]) for x in options]:
        if time_curr > time_max:
            continue
        pos = labels.index(person[1])
        idx = labels.index(p)
        time_spent = dist_matrix[pos][idx] + 1
        new_path = (time_curr+time_spent, (person[0], p))
        POI_COPY = POI.copy()
        POI_COPY.remove((p, f))
        new_q = sorted([queue[0], new_path], key=lambda x: x[0])
        solve_iter(graph, dist_matrix, POI_COPY, labels, results, new_q, path=path+[new_path])

    pressure = solve_path(path, graph)
    if pressure > results[0][0]:
        results[0] = (pressure, path)
    

def solve_path(path, graph, time_max=26):
    return sum([(time_max-time)*graph[where].flow for (time, (_, where)) in path])
    

def part_one(file_path):
    v_dict = {}
    edges = []
    headers = []
    with open(file_path, 'r') as file:
        for e, line in enumerate(file.read().splitlines(), 1):
            k, v , cs = parser(line)
            v_dict[k] = v
            for c in cs:
                edges.append((k, c))
            headers.append(k)
    results = []
    dist_matrix = floyd(e, edges, headers)
    POI = set([n.name for n in v_dict.values() if n.flow > 0])
   
    solve(v_dict, dist_matrix, POI, headers, results)
    return sorted(results)[-1][0]


def part_two(file_path):
    v_dict = {}
    edges = []
    headers = []
    with open(file_path, 'r') as file:
        for e, line in enumerate(file.read().splitlines(), 1):
            k, v , cs = parser(line)
            v_dict[k] = v
            for c in cs:
                edges.append((k, c))
            headers.append(k)
    results = [(0, [])]
    dist_matrix = floyd(e, edges, headers)
    POI = set([(n.name , n.flow )for n in v_dict.values() if n.flow > 0])
    persons = [("Me", "AA"), ("ELE", "AA")]

    solve_iter(v_dict, dist_matrix, sorted(POI, key=lambda x: x[1]), headers, results, [(0, x) for x in persons])
    return results[0][0] 
 

def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"{text} took {(end-start)*1000:>8.2f}ms : {result} ")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt") # Roughly 30 minutes, 
    

if __name__ == "__main__":
    main()
