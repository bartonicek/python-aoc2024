from typing import List
from dataclasses import dataclass

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

def coords_to_array(coords, ncol, nrow):
    out = [0 for _ in range(0, ncol * nrow)]
    for coord in coords:
        out[ncol * coord.y + coord.x] = 1
    return out

def print_coords(coords, ncol, nrow):
    out = [[0 for _ in range(0, ncol)] for _ in range(0, nrow)]
    for coord in coords:
        out[coord.y][coord.x] += 1
    for line in out: 
        line = [str("." if x == 0 else x) for x in line]
        print("".join(line))
    print("\n")

def calculate_centroid(coords):
    x, y = 0, 0
    for coord in coords:
        x += coord.x
        y += coord.y
    return Coords(x / len(coords), y / len(coords))

def avg_distance(coords):
    result = 0
    centroid = calculate_centroid(coords)

    for coord in coords:
        result += (coord.x - centroid.x) ** 2 + (coord.y - centroid.y) ** 2
    
    return result

distances = []

for j in range(0, 6446):
    for i in range(0, len(positions)):
        p = positions[i]
        v = velocities[i]

        p.x = (p.x + v.x) % ncol
        p.y = (p.y + v.y) % nrow


    print_coords(positions, ncol, nrow)
    distances.append(avg_distance(positions))

print(distances.index(min(distances)))

    








    



