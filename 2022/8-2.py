# Find highest scenic score possible for any tree

def get_scenic_score(map, i, j):
    if i == 0 or j == 0 or i == 98 or j == 98:
        return 0
        
    height = map[i][j]
    views = [
        map[i][:j][::-1],                    # Left
        map[i][j+1:],                        # Right
        [map[x][j] for x in range(i)][::-1], # Up
        [map[x][j] for x in range(i+1, 99)]  # Down
    ]
    
    score = 1
    for view in views:
        for idx, tree in enumerate(view, 1):
            if tree >= height:
                score *= idx
                break
        else:
            score *= len(view)
            
    return score

map = open("8-input.txt").read().splitlines()
scores = [[get_scenic_score(map, i, j) for j in range(99)] for i in range(99)]
max_score = max(max(row) for row in scores)

print(f"\nHighest scenic score: {max_score}")