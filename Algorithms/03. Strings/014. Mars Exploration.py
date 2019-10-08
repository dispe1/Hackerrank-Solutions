# Problem: https://www.hackerrank.com/challenges/mars-exploration/problem
# Difficulty : Easy
# Score : 15

import os

def marsExploration(s):
    ret = 0

    for i in range(len(s) // 3):
        if s[i*3] != 'S':
            ret += 1
        if s[i*3+1] != 'O':
            ret += 1
        if s[i*3+2] != 'S':
            ret += 1

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result))
    fptr.close()
