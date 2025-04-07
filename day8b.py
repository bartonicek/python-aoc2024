import math
from typing import List, Tuple, Dict, Set

file = open("./data/day8-test.txt", "r")
input = file.read()

node_positions: Dict[str, List[Tuple[int, int]]]  = {}
linewidth = input.index("\n") + 1
nlines = math.floor(len(input) / linewidth) + 1

class Grid:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set(self, mark, x, y):
        self.data[y][x] = mark
    
    def mark(self, mark, x, y):
        self.data[y][x] |= (1 << mark)

    def has(self, mark, x, y):
        return self.data[y][x] & (1 << mark) > 0
    
    def print(self):
        for i in range(0, len(self.data)): print(self.data[i])

node_count = 1
node_map = {}
mark_grid = Grid(nlines, linewidth - 1)
antinode_grid = Grid(nlines, linewidth - 1)

def mark_positions(mark, x, y):

    # Horizontal
    for i in range(0, linewidth - 1):
        if mark_grid.has(mark, i, y):
            print(mark, i, y)
            antinode_grid.set(1, i, y)
        mark_grid.mark(mark, i, y)
    
    # Vertical
    for i in range(0, nlines):
        if i == y: continue
        if mark_grid.has(mark, x, i):
            print(mark, x, i)
            antinode_grid.set(1, x, i)
        mark_grid.mark(mark, x, i)

    dx = max(x - y, 0)
    dy = max(y - x, 0)




    
for i in range(0, len(input)):
    char = input[i]
    if char == "." or char == "\n": continue

    if not char in node_map:
        node_map[char] = node_count
        node_count += 1

    mark = node_map[char]
    x, y = i % linewidth, math.floor(i / linewidth)

    mark_positions(mark, x, y)

print(antinode_grid.print())
