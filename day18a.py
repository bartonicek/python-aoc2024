from dataclasses import dataclass, field
from typing import List, Dict
import math
import heapq


file = open("./data/day18.txt", "r")
lines = file.read().split("\n")
lines.pop()
positions = [list(map(int, x.split(","))) for x in lines] 

width, height, nbytes = 71, 71, 1024

class Grid:
    data: List[str]

    def __init__(self, rows, cols):
        self.data = [["." for _ in range(cols)] for _ in range(rows)]

    def set(self, x, y, value):
        self.data[y][x] = value
    
    def get(self, x, y):
        if x < 0 or y < 0 or x >= len(self.data[0]) or y >= len(self.data): 
            return None
        return self.data[y][x]
    
    def print(self):
        print()
        for i in range(0, len(self.data)): print("".join(self.data[i]))

@dataclass(order=True)
class Coord:
    x: int
    y: int

    def __hash__(self):
        return (self.x << 16) | self.y
    
@dataclass(order=True)
class Node:
    dist: int
    coord: Coord

grid = Grid(width, height)

for i in range(0, nbytes):
    p = positions[i]
    grid.set(p[0], p[1], "#")

start = Coord(0, 0)
end = Coord(width - 1, height - 1)

def taxicab_dist(start: Coord, end: Coord): 
    return abs(start.x - end.x) + abs(start.y - end.y)

diffs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def find_neighbours(grid: Grid, coord: Coord) -> List[Coord]:
    result = []

    for d in diffs:
        v = grid.get(coord.x + d[0], coord.y + d[1])
        if v == None or v == "#": continue
        result.append(Coord(coord.x + d[0], coord.y + d[1]))

    return result

def reconstruct_path(previous: Dict[Coord, Coord], current: Coord):
    result = [current]

    while current in previous:
        current = previous[current]
        result.insert(0, current)
    
    return result

# A* algorithm
def find_path(grid: Grid, start: Coord, end: Coord, distfn):

    nodes = [Node(distfn(start, end), start)]
    previous: Dict[Coord, Coord] = {}

    gscore: Dict[Coord, int] = {}
    fscore: Dict[Coord, int] = {}

    gscore[start] = 0
    fscore[start] = distfn(start, end)

    while len(nodes) > 0:
        
        current = heapq.heappop(nodes)
        if current.coord == end: 
            return reconstruct_path(previous, current.coord)

        neighbours = find_neighbours(grid, current.coord)

        for neighbour in neighbours:
            candidate_gscore = gscore[current.coord] + 1

            if candidate_gscore < gscore.get(neighbour, math.inf):
                previous[neighbour] = current.coord
                gscore[neighbour] = candidate_gscore
                fscore[neighbour] = candidate_gscore + distfn(neighbour, end)

                node = Node(fscore[neighbour], neighbour)
                if not node in nodes: heapq.heappush(nodes, node)
                
    return None

path = find_path(grid, start, end, taxicab_dist)

for p in path:
    grid.set(p.x, p.y, "O")

grid.print()
print(len(path))