import math
from typing import List

file = open("./data/day11.txt", "r")
input = file.read()

def ndigits(x):                      # Handle 0
    return math.floor(max(math.log10(x + 0.1), 0)) + 1

def split(x: int):
    n = ndigits(x)
    # i = int(n / 2)
    # first = int(str(x)[0:i])
    # second = int(str(x)[i:n])
    h = 10 ** (n / 2)
    first = math.floor(x / h)
    second = x - first * h
    return first, second

def evolve(stones: List[int]):
    n = len(stones)
    for i in range(0, n):
        if stones[i] == 0: stones[i] = 1
        elif ndigits(stones[i]) % 2 == 0:
            first, second = split(stones[i])
            stones[i] = first
            stones.append(second)
        else:
            stones[i] *= 2024 

stones = [int(x) for x in input.split(" ")]

for i in range(0, 25):
    evolve(stones)

print(len(stones))

