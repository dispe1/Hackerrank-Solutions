# Problem: https://www.hackerrank.com/challenges/find-digits/problem
# Difficulty : Easy
# Score : 25

import os

def findDigits(n):
    answer = 0

    for s in str(n):
        i = int(s)
        if i != 0 and n % i == 0:
            answer += 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
