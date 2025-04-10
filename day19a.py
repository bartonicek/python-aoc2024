from typing import List, Dict

file = open("./data/day19.txt", "r")
input = file.read()
ps, ds = input.split("\n\n")

patterns = ps.split(", ")
designs = ds.split("\n")

def split(text: str, index: int):
    return text[:index], text[index:]

def try_split(target: str, patterns: List[str], seen: Dict[str, bool] = {}):
    if target in patterns: return True
    if len(target) == 1: return False

    any_split_works = False

    for i in range(1, len(target)):
        start, end = split(target, i)
        start_works, end_works = False, False

        if start in seen: start_works = seen[start]
        else:
            start_works = try_split(start, patterns, seen)
            seen[start] = start_works
        
        if end in seen: end_works = seen[end]
        else: 
            end_works = try_split(end, patterns, seen)
            seen[end] = end_works

        any_split_works = any_split_works or (start_works and end_works)
        if any_split_works: break

    return any_split_works

total = 0

for i in range(len(designs)):
    print(f"[{i}/{len(designs)}]")
    if try_split(designs[i], patterns): total += 1

print(total)

