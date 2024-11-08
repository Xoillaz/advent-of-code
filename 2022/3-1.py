# Each rusksack needs to contain exactly one type
# Need to find the share type in 2 compartments each rusksack
# Priority: a..z, A..Z = 1..26, 27..52
# Specify the sum of the priorities of the item types.

with open("3-input.txt", 'r') as file:
    seq = file.read().split('\n')

res = 0
for i in seq:
    mid = len(i) // 2
    share = set(i[:mid]) & set(i[mid:])
    x = list(share)[0]
    
    if x >= 'a' and x <= 'z':
        delta = ord(x) - ord('`')
    elif x >= 'A' and x <= 'Z':
        delta = ord(x) - ord('@') + 26 

    res += delta
    print(share, delta, res)
