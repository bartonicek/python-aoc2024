from typing import List
from dataclasses import dataclass
from functools import reduce

file = open("./data/day14.txt", "r")
input = file.read().split("\n")

nrow, ncol = 103, 101

@dataclass
class Coords:
    x: int
    y: int

positions: List[Coords] = []
velocities: List[Coords] = []

for i in range(0, len(input)):
    if input[i] == "": continue
    p, v = input[i].split(" ")

    pos = Coords(*[int(x) for x in p[2:].split(",")])
    vel = Coords(*[int(x) for x in v[2:].split(",")])

    positions.append(pos)
    velocities.append(vel)

positions_after_100 = []

for i in range(0, len(positions)):
    p = positions[i]
    v = velocities[i]

    p.x = (p.x + 100 * v.x) % ncol
    p.y = (p.y + 100 * v.y) % nrow

    positions_after_100.append(p)

def print_coords(coords, ncol, nrow):
    out = [[0 for _ in range(0, ncol)] for _ in range(0, nrow)]
    for coord in coords:
        out[coord.y][coord.x] += 1
    for line in out: 
        line = [str("." if x == 0 else x) for x in line]
        print("".join(line)) 

quadrants = [0, 0, 0, 0]

for p in positions_after_100:
    if p.x < int(ncol / 2) and p.y < int(nrow / 2): quadrants[0] += 1
    if p.x > int(ncol / 2) and p.y < int(nrow / 2): quadrants[1] += 1
    if p.x < int(ncol / 2) and p.y > int(nrow / 2): quadrants[2] += 1
    if p.x > int(ncol / 2) and p.y > int(nrow / 2): quadrants[3] += 1


print(quadrants)
print(reduce(lambda x, y: x * y, quadrants))

