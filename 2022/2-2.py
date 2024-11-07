# Rock Paper Scissors to decide whose camp is the closest to the snack storage
# 1 - Input: Decrypted Strategy Guide
# 2 - Score: the outcome of the round (0, 3, 6)
#       plus the shape you selected  (1, 2, 3)
# 3 - What would your total score be if everything goes exactly according to your strategy guide?

res = 0

with open("2-input.txt", 'r') as file:
    seq = file.read().split('\n')

for i in seq:
    a, b = ['A', 'B', 'C'].index(i[0]), ['X', 'Y' ,'Z'].index(i[2])
    
    # Rule: index 0 > 2 > 1 > 0 ..
    if b == 2: 
        res += (a + 1) % 3 + 7 # Case Win
    elif b == 1: 
        res += a + 4 # Case Draw
    elif b == 0:
        res += (a - 1) % 3 + 1 # Case Lose

    print(res)
