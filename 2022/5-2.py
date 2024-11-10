# The marked crates need to be rearranged.
# The CrateMover 9001 is capable of moving multiple crates at once.
# After the procedure completes, what crate ends up on top of each stack?

import re

stk = ["",
    "VCDRZGBW",
    "GWFCBSTV",
    "CBSNW",
    "QGMNJVCP",
    "TSLFDHB",
    "JVTWMN",
    "PFLCSTG",
    "BDZ",
    "MNZW"
]

with open("5-input.txt", 'r') as file:
    seq = file.read().split('\n')

for i in range(len(seq)-1):
    _, i, a, b = re.split('\D+', seq[i])
    i, a, b = int(i), int(a), int(b)
    print(a, i, b)
    
    print(stk[a], stk[b])

    stk[b] += stk[a][-i:]
    stk[a] = stk[a][:-i]
    
    print(stk[a], stk[b], end='\n\n')

print(stk)