# Problem: https://www.hackerrank.com/challenges/cavity-map/problem
# Difficulty : Easy
# Score : 30

import os

def cavityMap(grid):
    change = []

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                change.append([i, j]);

    grid = [list(i) for i in grid]

    for c in change:
        grid[c[0]][c[1]] = 'X'

    grid = [''.join(i) for i in grid]

    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.close()
