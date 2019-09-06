# Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Difficulty : Easy
# Score : 10

import os

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        total = sum(s[i:m+i])
        if total == d:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result))
    fptr.close()
