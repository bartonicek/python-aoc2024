import math
from typing import List, Dict

file = open("./data/day11.txt", "r")
input = file.read()

def ndigits(x):                      # Handle 0
    return math.floor(max(math.log10(x + 0.1), 0)) + 1

def split(x: int):
    n = ndigits(x)
    h = 10 ** (n / 2)
    first = math.floor(x / h)
    second = int(x - first * h)
    return first, second


def evolve(stones: Dict[int, int]):
    new_stones = { 0: 0, 1: 0 }
    
    for k, v in stones.items():
        if k == 0: new_stones[1] += v
        elif ndigits(k) % 2 == 0:
            first, second = split(k)
            new_stones[first] = new_stones.get(first, 0) + v
            new_stones[second] = new_stones.get(second, 0) + v
        else:
            new_stones[k * 2024] = v

    stones.clear()
    stones.update(new_stones)


stones = dict([[int(x), 1] for x in input.split(" ")])

for _ in range(0, 75):
    evolve(stones)
    
print(sum(stones.values()))
