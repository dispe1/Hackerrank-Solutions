# Problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem
# Difficulty : Medium
# Score : 20

import os
import collections


def nonDivisibleSubset(k, s):
    dic = collections.Counter()

    for i in s:
        dic[i % k] += 1

    answer = min(dic[0], 1)

    for r in range(1,k//2+1):
        if r != k/2:
            answer += max(dic[r], dic[k-r])

    if k % 2 == 0:
        answer += 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result))
    fptr.close()
