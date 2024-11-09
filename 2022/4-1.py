# There are overlaps in assignments of Elves
# In how many assignment pairs does one range fully contain the other?

import re

with open("4-input.txt", 'r') as file:
    seq = file.read().split('\n')

res = 0
for i in range(len(seq) - 1): # Exception: The last item is empty.
    arr = re.split('\D', seq[i])
    a, b = int(arr[0]), int(arr[1])
    c, d = int(arr[2]), int(arr[3])
    if (a >= c and b <= d) or (b >= d and a <= c):
        res += 1
        print(a, b, c, d, res)

print(res)
