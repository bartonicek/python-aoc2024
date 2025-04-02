import math
from typing import List, Tuple, Dict, Set

file = open("./data/day8.txt", "r")
input = file.read()

node_positions: Dict[str, List[Tuple[int, int]]]  = {}
linewidth = input.index("\n") + 1

for i in range(0, len(input)):
    char = input[i]
    if char == "." or char == "\n": continue

    pos: Tuple[int, int] = (i % linewidth, math.floor(i / linewidth))
    if not char in node_positions: node_positions[char] = []
    node_positions[char].append(pos)

def is_outside(pos: Tuple[int, int], bounds: Tuple[int, int]):
    return pos[0] < 0 or pos[0] >= bounds[0] or pos[1] < 0 or pos[1] >= bounds[1]

antinode_set: Set[Tuple[int, int]] = set()

def count_antinodes(positions: List[Tuple[int, int]], bounds: Tuple[int, int]):
    total = 0

    for i in range(0, len(positions)):
        for j in range(i + 1, len(positions)):
            
            pos1 = positions[i]
            pos2 = positions[j]

            diff1 = (pos1[0] - pos2[0], pos1[1] - pos2[1])
            diff2 = (pos2[0] - pos1[0], pos2[1] - pos1[1])

            anti_pos1 = (pos1[0] + diff1[0], pos1[1] + diff1[1])
            anti_pos2 = (pos2[0] + diff2[0], pos2[1] + diff2[1])

            if not is_outside(anti_pos1, bounds) and not anti_pos1 in antinode_set: 
                antinode_set.add(anti_pos1)                
                total += 1
            
            if not is_outside(anti_pos2, bounds) and not anti_pos2 in antinode_set:
                antinode_set.add(anti_pos2)
                total += 1

    return total

total = 0
bounds = [linewidth - 1, math.floor(len(input) / linewidth)]

for k, v in node_positions.items():
    total += count_antinodes(v, bounds)

print(total)