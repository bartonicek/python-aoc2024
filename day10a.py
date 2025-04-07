file = open("./data/day10-test.txt", "r")
input = file.read()

map = [[int(y) for y in list(x)] for x in input.split("\n")]

def try_elevation(map, i, j, elevation):
    if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]): return 0
    if elevation == 6 and map[i][j] == 6: return 1
    if map[i][j] != elevation: return 0

    e = elevation + 1
    return (try_elevation(map, i - 1, j, e) + try_elevation(map, i + 1, j, e) +
        try_elevation(map, i, j - 1, e) + try_elevation(map, i, j + 1, e))


# for i in range(0, len(map)):
#     for j in range(0, len(map[0])):
#         if map[i][j] != 0: continue
#         print("foo") 
