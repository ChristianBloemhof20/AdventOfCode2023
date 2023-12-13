import sys
with open('input.txt' if len(sys.argv) == 1 else 'input.txt') as f: file = f.read()
patterns = file.split('\n\n')

def f(grid): 
    for i in range(len(grid)-1):
        tops, bottoms = [], []
        t, b = i, i+1
        while t >= 0 and b <= len(grid)-1:
            tops.append(grid[t])
            bottoms.append(grid[b])
            t -= 1
            b += 1
        if sum(1 for top, bottom in zip(tops, bottoms) for t, b in zip(top, bottom) if t != b) == 1:
            print(i+1)
            return i + 1
    return 0

rows, cols = 0, 0
for pattern in patterns: 
    lines = pattern.split('\n')
    grid = [[c for c in line] for line in lines]
    rows += f(grid) 
    cols += f(list(zip(*grid)))
print(cols + 100*rows)