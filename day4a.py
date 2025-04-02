import math

file = open("./data/day4.txt", "r")
input = file.read()

directions = [
    [1, 0], [-1, 0], # x-axis
    [0, 1], [0, -1], # y-axis
    [1, 1], [-1, -1], # right diagonal
    [1, -1], [-1, 1] # left diagonal
    ]

def is_outside(pos, bounds):
    return pos[0] < 0 or pos[0] >= bounds[0] or pos[1] < 0 or pos[1] >= bounds[1]

def char_at_pos(x, pos, linewidth):
    return x[pos[1] * linewidth + pos[0]]

def count_xmas(x: str, i: int, linewidth: int):
    pos = [i % linewidth, math.floor(i / linewidth)]
    bounds = [linewidth - 1, math.floor(len(x) / linewidth)]
    chars = "MAS"

    total = 0

    for d in directions:
        new_pos = pos.copy()
        is_xmas = True

        for i in range(0, 3):
            new_pos[0] += d[0]
            new_pos[1] += d[1]

            if (is_outside(new_pos, bounds)): 
                is_xmas = False
                break

            if char_at_pos(x, new_pos, linewidth) != chars[i]: 
                is_xmas = False
                break

        if is_xmas: total += 1
    
    return total
            
total = 0
linewidth = input.index("\n") + 1
    
for i in range(0, len(input)):
    if input[i] != "X": continue
    total += count_xmas(input, i, linewidth)

print(total)
