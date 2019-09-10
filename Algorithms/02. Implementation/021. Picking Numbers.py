# Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
# Difficulty : Easy
# Score : 20

import os
import collections

def pickingNumbers(a):
    c = collections.Counter(a)
    answer = 0
    
    for key, value in c.items():
        if key-1 in c:
            if value + c[key-1] > answer:
                answer = value+c[key-1]

        if value > answer:
            answer = value

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result))
    fptr.close()
