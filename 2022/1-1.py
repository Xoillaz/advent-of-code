# 2022-D1: Calorie Counting
# 1 - Input indicates foods carried.
# 2 - Find the Elf carrying the most Calories. How much does it equip?

with open('input.txt', 'r') as file:
    seq = file.read().split('\n') # Read file, turn into a list.

res, cal = 0, 0
for i in seq:
    if len(i) == 0: # Condition: Empty Line
        res = cal if cal > res else res # Compare which is the greatest sum.
        cal = 0
    else:
        cal += int(i)

print(res)
