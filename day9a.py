is_file = open("./data/day9.txt", "r")
input = is_file.read().replace("\n", "")

slots = []

id, is_file = 0, True
counts = [int(x) for x in list(input)]
slots = []

EMPTY = -99

for count in counts:
    if is_file:
        for _ in range(0, count): slots.append(id)
        id += 1
        is_file = False
    else:
        for _ in range(0, count): slots.append(EMPTY)
        is_file = True

i, j = 0, len(slots) - 1

while True:
    while not slots[i] == EMPTY: i += 1
    while slots[j] == EMPTY: j -= 1
    if i >= j: break
    slots[i], slots[j] = slots[j], slots[i]

checksum, i = 0, 0
while slots[i] != EMPTY: 
    checksum += i * slots[i]
    i += 1

print(checksum)
