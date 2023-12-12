import networkx as nx

mapping = {
    "|":  [(0-1, 0), (0+1, 0)],
    "-":  [(0, 0-1), (0, 0+1)],
    "L":  [(0-1, 0), (0, 0+1)],
    "J":  [(0-1, 0), (0, 0-1)],
    "7":  [(0, 0-1), (0+1, 0)],
    "F":  [(0, 0+1), (0+1, 0)]
}


def create_graph(file_path):
    graph = nx.DiGraph()
    with open(file_path, 'r') as file:
        for row, line in enumerate(file.read().strip().splitlines()):
            for col, char in enumerate(line):
                loc = (row, col)
                graph.add_node(loc, char=char)
                match char:
                    case "|":
                        graph.add_edge((row, col), (row-1,col))
                        graph.add_edge((row, col), (row+1, col))
                    case "-":
                        graph.add_edge((row, col), (row, col-1))
                        graph.add_edge((row, col), (row, col+1))
                    case "L":
                        graph.add_edge((row, col), (row-1, col))
                        graph.add_edge((row, col), (row, col+1))
                    case "J":
                        graph.add_edge((row, col), (row-1, col))
                        graph.add_edge((row, col), (row, col-1))
                    case "7":
                        graph.add_edge((row, col), (row, col-1))
                        graph.add_edge((row, col), (row+1, col))
                    case "F":
                        graph.add_edge((row, col), (row, col+1))
                        graph.add_edge((row, col), (row+1, col))
                    case "S":
                        source = (row, col)
                        graph.add_edge((row, col), (row, col+1))
                        graph.add_edge((row, col), (row, col-1))
                        graph.add_edge((row, col), (row+1, col))
                        graph.add_edge((row, col), (row-1, col))
                    case _:
                        graph.remove_node(loc)
                        continue
    return graph, source, row, col

def part_one(file_path):
    graph, source, _, _ = create_graph(file_path)
    removal = []
    un_graph = graph.to_undirected(reciprocal=True)
    sub_nodes = nx.descendants(un_graph, source) | {source}
    sub_graph = un_graph.subgraph(sub_nodes)
    target = list(nx.bfs_edges(sub_graph, source))[-1][-1]
    path = nx.shortest_path(sub_graph, source, target)
    return len(path)-1


def part_two(file_path):
    graph, source, max_y, max_x = create_graph(file_path)
    removal = []
    un_graph = graph.to_undirected(reciprocal=True)
    sub_nodes = nx.descendants(un_graph, source) | {source}
    sub_graph = un_graph.subgraph(sub_nodes)
    node_list = sorted(sub_graph.nodes(data=True))
    changes = [
        tuple(map(lambda i, j: i - j, x[1], x[0]))
        for x in sub_graph.edges(source)
    ]
    new_key = [k for k, v in mapping.items() if v == changes][0]
    nx.set_node_attributes(sub_graph, {source: {"char": new_key}})

    tiles = 0
    for r in range(max_y+1):
        for c in range(max_x+1):
            location = (r, c)
            if location in sub_graph.nodes:
                continue
            else:
                main_row = filter(lambda x: x[0][0] == r, node_list)
                moving_through = list(filter(lambda x: x[0][1] <= c, main_row))[::-1]
                chars = [x[1]['char'] for x in moving_through]
                chars = "".join(filter(lambda x: x != "-", chars))
                chars = chars.replace("7F", "").replace("JL", "") # Remove the pipes over which you can walk
                chars = chars.replace("JF", "|").replace("7L", "|") # Change the pipes to "boundary"  pipe
                tiles += len(chars) % 2
    return tiles


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 1T bigger input", part_one, "test_2.txt")
    timed_print("Solution 2T", part_two, "test.txt")   
    timed_print("Solution 2T bigger input", part_two, "test_3.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
