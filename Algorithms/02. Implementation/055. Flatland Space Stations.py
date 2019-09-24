# Problem: https://www.hackerrank.com/challenges/flatland-space-stations/problem
# Difficulty : Easy
# Score : 25

import os

def flatlandSpaceStations(n, m, c):
    c.sort()
    maximum = max(c[0], n - c[-1] - 1) # initialize with ends

    for i in range(1, m):
        d = c[i] - c[i-1]
        maximum = max(d//2, maximum)

    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, m, c)

    fptr.write(str(result))
    fptr.close()
