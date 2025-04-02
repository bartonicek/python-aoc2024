from typing import List

file = open("./data/day2.txt", "r")

def is_bad_diff(diff: int, sign: int):
    return diff == 0 or sign * diff < 0 or abs(diff) > 3

def clamp(x: int, vmin: int, vmax: int):
    max(min(x, vmax), vmin)

def is_safe_skip(x: List[int], skip: int):
    x = x.copy()
    x.pop(skip)

    sign = max(min(x[0] - x[1], 1), -1)

    if sign == 0: return False

    for i in range(0, len(x) - 1):
        diff = x[i] - x[i + 1]
        if is_bad_diff(diff, sign): return False

    return True

total = 0

for line in file:
    values = [int(x) for x in line.split()]
    for i in range(0, len(values)):
        if is_safe_skip(values, i): 
            total += 1
            break

print(total)

