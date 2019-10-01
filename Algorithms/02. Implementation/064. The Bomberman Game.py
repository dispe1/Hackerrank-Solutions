# Problem: https://www.hackerrank.com/challenges/bomber-man/problem
# Difficulty : Medium
# Score : 40

import os

def bomberMan(n, grid):
    row, col = len(grid), len(grid[0])

    if n < 2 : return grid

    if n % 2 == 0: return ['O' * col for _ in range(row)]

    def boom():
        g = [list(i) for i in grid]

        for i in range(row):
            for j in range(col):
                if g[i][j] == 'O':
                    for x,y in (i,j+1), (i,j-1),(i+1, j), (i-1,j):
                        if 0 <= x < row and 0 <= y < col and g[x][y] == '.':
                           g[x][y] = 'X'
                    g[i][j] = 'X'

        return [''.join('.' if j == 'X' else 'O' for j in i) for i in g]

    grid = boom()
    return grid if n % 4 == 3 else boom()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()
    r = int(rcn[0])
    c = int(rcn[1])
    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.close()
