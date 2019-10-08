# Problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# Difficulty : Easy
# Score : 20

import os

def hackerrankInString(s):
    ret = 'NO'
    target = 'hackerrank'
    idx = 0

    for c in s:
        if c == target[idx]:
            idx += 1
        if idx == len(target):
            ret = 'YES'
            break

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
