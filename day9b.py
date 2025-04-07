from dataclasses import dataclass
from typing import List

file = open("./data/day9.txt", "r")
input = file.read().replace("\n", "")

EMPTY = -99

@dataclass
class Slot:
    value: int
    count: int

def slots_to_string(slots: List[Slot]):
    string = ""
    for slot in slots:
        symbol = "." if slot.value == EMPTY else slot.value
        string += "".join([str(symbol) for _ in range(0, slot.count)])
    return string



slots: List[Slot] = []
id, is_file = 0, True
counts = [int(x) for x in list(input)]

for count in counts:
    if is_file:
        slots.append(Slot(id, count))
        id += 1
        is_file = False
    else:
        slots.append(Slot(EMPTY, count))
        is_file = True

i, j = 0, len(slots) - 1

while j > 0:
    i = 0

    # Find first value slot from end of the list
    while slots[j].value == EMPTY: j -= 1

    # Find first empty slot which can fit it
    while i < j:

        # Merge empty slots
        if slots[i].value == EMPTY and slots[i + 1].value == EMPTY:
            slots[i].count += slots[i + 1].count
            slots.pop(i + 1)

        if (slots[i].value == EMPTY and
            slots[i].count >= slots[j].count): break 
        i += 1
    
    if (i == j): j -= 1; continue # No slots can fit

    vals = slots[j]

    slots[i].count -= vals.count
    slots[j] = Slot(EMPTY, vals.count)
    slots.insert(i, vals)

    print(j)
    j += 1

checksum = 0
index = 0

vals = []
for slot in slots:
    vals += [slot.value for _ in range(0, slot.count)]

total = 0
for i in range(0, len(vals)):
    if vals[i] == EMPTY: continue
    total += i * vals[i]

print(total)












# checksum, i = 0, 0
# while slots[i] != EMPTY: 
#     checksum += i * slots[i]
#     i += 1

# print(checksum)
