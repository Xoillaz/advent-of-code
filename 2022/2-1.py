# Rock Paper Scissors to decide whose camp is the closest to the snack storage
# 1 - Input: Encrypted Strategy Guide
# 2 - Score; each round is the shape you selected  (1, 2, 3)
#       plus the score for the outcome of the round (0, 3, 6)
# 3 - What would your total score be if everything goes exactly according to your strategy guide?

res = 0

with open("2-input.txt", 'r') as file:
    seq = file.read().split('\n')

for i in seq:
    a, b = ['A', 'B', 'C'].index(i[0]), ['X', 'Y' ,'Z'].index(i[2])
    res += b + 1 # Score: The shape I selected
    
    # Rule: index 1 > 3 > 2 > 1 ..
    # Score: The outcome of the round
    if b - a == 1 or b - a == -2: # Case Win
        res += 6
    elif a == b: # Case Draw
        res += 3
    elif a - b == 1 or a - b == -2: # Case Lose
        res += 0

    print(res)
