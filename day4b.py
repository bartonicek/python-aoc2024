import math

file = open("./data/day4.txt", "r")
input = file.read()

directions = [
    [1, 1], [-1, -1], # right diagonal
    [1, -1], [-1, 1] # left diagonal
    ]

def is_outside(pos, bounds):
    return pos[0] < 0 or pos[0] >= bounds[0] or pos[1] < 0 or pos[1] >= bounds[1]

def char_at_pos(x, pos, linewidth):
    return x[pos[1] * linewidth + pos[0]]    

def is_xmas(x: str, i: int, linewidth: int):
    pos = [i % linewidth, math.floor(i / linewidth)]
    bounds = [linewidth - 1, math.floor(len(x) / linewidth)]
    found = True

    for i in range(0, 2):
        dir = directions[2 * i]
        opp = directions[2 * i + 1]

        pos1 = [pos[0] + dir[0], pos[1] + dir[1]]
        pos2 = [pos[0] + opp[0], pos[1] + opp[1]]

        if is_outside(pos1, bounds) or is_outside(pos2, bounds): 
            found = False
            continue

        char1 = char_at_pos(x, pos1, linewidth)
        char2 = char_at_pos(x, pos2, linewidth)

        if not ((char1 == "M" and char2 == "S") or (char1 == "S" and char2 == "M")):
            found = False

    return found
            
total = 0
linewidth = input.index("\n") + 1
    
for i in range(0, len(input)):
    if input[i] != "A": continue
    if is_xmas(input, i, linewidth): total += 1

print(total)
