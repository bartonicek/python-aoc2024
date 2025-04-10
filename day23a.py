from typing import Dict, Set

file = open("./data/day23.txt", "r")
input = file.read().split("\n")
input.pop()

pairs = [x.split("-") for x in input]

computers = set()
connections: Dict[str, Set[str]] = {}

for pair in pairs:
    first, second = pair

    computers.add(first)
    computers.add(second)

    if connections.get(first) == None: connections[first] = set()
    if connections.get(second) == None: connections[second] = set()

    connections[first].add(second)
    connections[second].add(first)

start_with_t = list(filter(lambda x: x[0] == "t", computers))

def threeway_connections(connections: Dict[str, Set[str]], conn: str):
    triples = set()
    set1 = connections[conn]

    for conn2 in set1:
        set2 = connections[conn2]
        intersection = set1.intersection(set2)
        if len(intersection) == 0: continue

        for conn3 in set2: 
            set3 = connections[conn3]
            if not conn in set3: continue

            conns = [conn, conn2, conn3]
            conns = "-".join(sorted(conns))
            triples.add(conns)

    return triples

all_threeway_conns = set()

for conn in start_with_t:
    conns = threeway_connections(connections, conn)
    for c in conns: all_threeway_conns.add(c)

print(len(all_threeway_conns))






