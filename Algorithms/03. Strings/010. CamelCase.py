# Problem: https://www.hackerrank.com/challenges/camelcase/problem
# Difficulty : Easy
# Score : 15

import os

def camelcase(s):
    ret = 1

    for i in s:
        if 'A' <= i <= 'Z':
            ret += 1

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result))
    fptr.close()
