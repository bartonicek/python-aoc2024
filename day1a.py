from typing import List

file = open("./data/day1.txt", "r")

list1: List[int] = []
list2: List[int] = []

for line in file:
    [left, right] = line.split()
    list1.append(int(left))
    list2.append(int(right))

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += (abs(list1[i] - list2[i]))

print(total)
