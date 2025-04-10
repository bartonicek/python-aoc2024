from dataclasses import dataclass
from typing import List, Dict
import math
import heapq

file = open("./data/day18.txt", "r")
lines = file.read().split("\n")
lines.pop()
positions = [list(map(int, x.split(","))) for x in lines] 

width, height = 71, 71

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
    
    def clear(self):
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                self.data[y][x] = "."
    
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

    distance_to_coord: Dict[Coord, int] = {}
    expected_distance: Dict[Coord, int] = {}

    distance_to_coord[start] = 0
    expected_distance[start] = distfn(start, end)

    while len(nodes) > 0:
        
        current = heapq.heappop(nodes)
        if current.coord == end: 
            return reconstruct_path(previous, current.coord)

        neighbours = find_neighbours(grid, current.coord)

        for neighbour in neighbours:
            candidate_distance = distance_to_coord[current.coord] + 1

            if candidate_distance < distance_to_coord.get(neighbour, math.inf):
                previous[neighbour] = current.coord
                distance_to_coord[neighbour] = candidate_distance
                expected_distance[neighbour] = candidate_distance + distfn(neighbour, end)

                node = Node(expected_distance[neighbour], neighbour)
                if not node in nodes: heapq.heappush(nodes, node)
                
    return None

grid = Grid(width, height)

def update_grid(grid: Grid, positions):
    grid.clear()
    for p in positions: grid.set(p[0], p[1], "#")


i, j = 0, len(positions)

# Binary search
while i < j:
    mid = int((i + j) / 2)
    update_grid(grid, positions[:mid])
    
    path = find_path(grid, start, end, taxicab_dist)
    
    if path == None: j = mid
    else: i = mid + 1

# update_grid(grid, positions[:i])
# print(find_path(grid, start, end, taxicab_dist))
# grid.print()

# update_grid(grid, positions[:(i - 1)])
# print(find_path(grid, start, end, taxicab_dist))
# grid.print()

print(positions[i - 1])