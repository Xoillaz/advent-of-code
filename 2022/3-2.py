# Each rusksack needs to contain exactly one type
# Need to find the share type in each 3 rusksack
# Priority: a..z, A..Z = 1..26, 27..52
# Specify the sum of the priorities of the item types.

with open("3-input.txt", 'r') as file:
    seq = file.read().split('\n')

i, res = 0, 0
for i in range(2, len(seq), 3):
    share = set(seq[i-2]) & set(seq[i-1]) & set(seq[i])
    x = list(share)[0]
    
    if x >= 'a' and x <= 'z':
        delta = ord(x) - ord('`')
    elif x >= 'A' and x <= 'Z':
        delta = ord(x) - ord('@') + 26 

    res += delta
    print(share, delta, res)
