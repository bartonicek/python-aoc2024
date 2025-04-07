from dataclasses import dataclass
from typing import List

file = open("./data/day15.txt", "r")
map, moves = file.read().split("\n\n")

map = [list(x) for x in map.split("\n")]

def print_map(map: List[List[str]]):
    for row in map: print("".join(row))
    print("\n")

@dataclass
class Coords:
    x: int
    y: int

pos = Coords(0, 0)

for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == "@":
            pos.x = j
            pos.y = i
            break

moves = list(moves)

def next_position(orig: Coords, dest: Coords):
    return Coords(2 * dest.x - orig.x, 2 * dest.y - orig.y)

def try_swap(map: List[List[str]], orig: Coords, dest: Coords):
    if orig.x == dest.x and orig.y == dest.y: return orig
    if (dest.x < 0 or dest.y < 0 or 
        dest.x >= len(map[0]) or dest.y >= len(map)): return orig
    if map[dest.y][dest.x] == "#": return orig
    if map[dest.y][dest.x] == ".":
        map[dest.y][dest.x] = map[orig.y][orig.x]
        map[orig.y][orig.x] = "."
        return dest
    if map[dest.y][dest.x] == "O":
        new_target = next_position(orig, dest)
        try_swap(map, dest, new_target)
        if map[dest.y][dest.x] != ".": return orig
        map[dest.y][dest.x] = map[orig.y][orig.x]
        map[orig.y][orig.x] = "."
        return dest

for move in moves:
    if move == "<": pos = try_swap(map, pos, Coords(pos.x - 1, pos.y))
    elif move == ">": pos = try_swap(map, pos, Coords(pos.x + 1, pos.y))
    elif move == "^": pos = try_swap(map, pos, Coords(pos.x, pos.y - 1))
    elif move == "v": pos = try_swap(map, pos, Coords(pos.x, pos.y + 1))

def compute_score(map):
    result = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == "O": result += i * 100 + j
    return result

print(compute_score(map))
    

