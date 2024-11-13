# How many trees are visible from outside the grid?

def crossCheck(map, i, j):
    if i == 0 or j == 0 or i == 98 or j == 98:
        return True
    else:
        L, R = map[i][:j], map[i][j+1:]
        U = [map[x][j] for x in range(i)]
        D = [map[x][j] for x in range(i+1, 99)]
        return min(max(set(L)), max(set(R)), max(set(U)), max(set(D))) < map[i][j]

map = open("8-input.txt").read().splitlines()
is_visible = [[-1 for j in range(99)] for i in range(99)]
res = 0

for i in range(99):
    for j in range(99):
        is_visible[i][j] = 1 if crossCheck(map, i, j) else 0
        res += is_visible[i][j]

for line in is_visible:
    for item in line:
        print('.' if item == 0 else '#', end="")
    print()

print(res)