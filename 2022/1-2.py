# 2022-D1: Calorie Counting
# 1 - Input indicates foods carried.
# 2 - Find the top 3 Elves carrying the most Calories. How much are those Elves carrying in total?

with open('input.txt', 'r') as file:
    seq = file.read().split('\n') # Read file, turn into a list.

cal = 0
res = [0, 0, 0]
for i in seq:
    if len(i) == 0: # Condition: Empty Line
        if cal > res[0]:
            res[1], res[0] = res[0], cal
        elif cal > res[1]:
            res[2], res[1] = res[1], cal
        elif cal > res[2]:
            res[2] = cal
        cal = 0
    else:
        cal += int(i)

print(res, sum(res))
