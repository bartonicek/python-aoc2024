from typing import List, Dict

file = open("./data/day19.txt", "r")
input = file.read()
ps, ds = input.split("\n\n")

patterns = ps.split(", ")
designs = ds.split("\n")
designs.pop()

def split(text: str, index: int):
    return text[:index], text[index:]

def count_splits(target: str, patterns: List[str], counts: Dict[str, bool] = {}):
    if len(target) == 0: return 1
    if len(target) == 1: return 1 if target in patterns else 0
    if target in counts: return counts[target]

    # Two (non-mutually exclusive) possibilities:
    # 1. Patterns are in the left and right halves of the target
    # 2. There are patterns that cross the midpoint (may be the whole target)

    mid = len(target) // 2
    total_count = 0

    # Case 1: Left and right halves
    left = count_splits(target[:mid], patterns, counts)
    right = count_splits(target[mid:], patterns, counts)
    total_count += left * right

    # Case 2: Patterns that cross the midpoint
    for pattern in patterns:
        if not 1 < len(pattern) <= len(target): continue

        for i in range(len(pattern) - 1):
            start = mid - i - 1
            end = start + len(pattern)
            if not target[start:end] == pattern: continue
            
            left = count_splits(target[:start], patterns, counts)
            right = count_splits(target[end:], patterns, counts)
            total_count += left * right

    counts[target] = total_count
    return total_count

total = 0
counts = {}

for i in range(len(designs)):
    print(f"[{i}/{len(designs)}]")
    total += count_splits(designs[i], patterns, counts)

print(total)
