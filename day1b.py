from typing import List

file = open("./data/day1.txt", "r")

list1: List[int] = []
list2: List[int] = []

for line in file:
    [left, right] = line.split()
    list1.append(int(left))
    list2.append(int(right))

counts = {}

for v in list2:
    if not v in counts: counts[v] = 0
    counts[v] += 1

total = 0

for v in list1:
    if not v in counts: continue
    total += v * counts[v]

print(total)