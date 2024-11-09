# There are overlaps in assignments of Elves
# In how many assignment pairs do the overlap?
import re

with open("4-input.txt", 'r') as file:
    seq = file.read().split('\n')

res = 0
for i in range(len(seq) - 1): # Exception: The last item is empty.
    a, b, c, d = [int(i) for i in re.split('\D', seq[i])]

    if a >= c and b <= d: # B fully contains A.
        res += 1
    elif b >= d and a <= c: # A fully contains B.
        res += 1
    elif a < c and c <= b and b <= d: # A's tail was overlaped.
        res += 1
    elif c < a and a <= d and d <= b: # B's tail was overlaped.
        res += 1

print(res)
