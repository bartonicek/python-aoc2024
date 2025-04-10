from typing import Dict, Set

file = open("./data/day23.txt", "r")
input = file.read().split("\n")
input.pop()

pairs = [x.split("-") for x in input]

computers = set()
connection_graph: Dict[str, Set[str]] = {}

for pair in pairs:
    first, second = pair

    computers.add(first)
    computers.add(second)

    if connection_graph.get(first) == None: connection_graph[first] = set()
    if connection_graph.get(second) == None: connection_graph[second] = set()

    connection_graph[first].add(second)
    connection_graph[second].add(first)

def connected_neighbours(graph: Dict[str, Set[str]], conn: str):
    candidates = list(graph[conn])
    exclude_dict: Dict[str, Set[str]] = {}

    for i in range(0, len(candidates)):
        exclude_dict[candidates[i]] = set()
        for j in range(0, len(candidates)):
            if i == j: continue
            if candidates[j] in graph[candidates[i]]: continue 
            exclude_dict[candidates[i]].add(candidates[j])

    max_len = 0
    for v in exclude_dict.values(): max_len = max(max_len, len(v))

    result = graph[conn].copy()

    for k, v in exclude_dict.items():
        if (len(v) == max_len): 
            result.discard(k)
            continue
        result = result.difference(v)

    result.add(conn)
    return result

max_len = 1
lan_party = set()

for c in computers:
    neighbours = connected_neighbours(connection_graph, c)
    if len(neighbours) > max_len: 
        max_len = len(neighbours)
        lan_party = neighbours

print(",".join(list(sorted(lan_party))), max_len)
    











