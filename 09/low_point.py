import math

with open('input.txt', 'r') as input:
    grid = [list(map(int, row)) for row in input.read().split('\n')]

groups = []
def count_groups(i, j):
    if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[0]) or grid[j][i] == 9 or grid[j][i] == -1:
        return
    grid[j][i] = -1
    groups[len(groups)-1] += 1
    count_groups(i+1, j)
    count_groups(i-1, j)
    count_groups(i, j+1)
    count_groups(i, j-1)
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        groups.append(0)
        count_groups(j, i)
print(math.prod(sorted(groups, reverse=True)[:3]))