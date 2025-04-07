from dataclasses import dataclass
from decimal import Decimal

file = open("./data/day13.txt", "r")
input = file.read().split("\n\n")

@dataclass
class Coords:
    x: int
    y: int

@dataclass 
class Machine:
    button1: Coords
    button2: Coords
    coords: Coords

def process_button(string):
    xs, ys = string.split(": ")[1].split(", ")
    return Coords(int(xs[2:]), int(ys[2: ]))

offset = 10000000000000

def process_coords(string):
    xs, ys = string.split(": ")[1].split(", ")
    return Coords(int(xs[2:]) + offset, int(ys[2:]) + offset)

def process_machine(string):
    lines = string.split("\n")

    b1 = process_button(lines[0])
    b2 = process_button(lines[1])
    coords = process_coords(lines[2])

    return Machine(b1, b2, coords)

# Let b1 and b2 be vectors corresponding to 
# the two buttons, and z be the vector corresponding
# to the machine coordinates.
# 
# We want t * b1 + u * b2 = z, for t, u >= 0
# 
# i.e. appending a multiple of b1 to a multiple 
# of b2 gives us c.

def solve_machine(machine: Machine):
    but1, but2 = machine.button1, machine.button2
    a, b, c, d = but1.x, but2.x, but1.y, but2.y
    z = machine.coords

    det = (a * d) - (b * c)
    if det == 0: return -1, -1

    b1 = Decimal(d * z.x - b * z.y) / det
    b2 = Decimal(-(c * z.x) + a * z.y) / det

    return b1, b2

def is_valid(presses):
    return presses >= 0 and presses % 1 == 0

total = 0

for m in input:
    if m == "": continue
    machine = process_machine(m)
    b1, b2 = solve_machine(machine)

    if not is_valid(b1) or not is_valid(b2): continue

    total += 3 * b1 + b2

print(total)


