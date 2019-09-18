# Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Difficulty : Medium
# Score : 35

import os

def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

def biggerIsGreater(w):
    answer = 'no answer'

    if list(w) == sorted(w, reverse = True):
        return answer

    for i in range(len(w)-1, -1, -1):
        if w[i] > w[i-1]:
            for j in range(len(w)-1, i-1, -1):
                if w[j] > w[i-1]:
                    w = swap(w, j, i-1)
                    answer = w[:i] + ''.join(reversed(w[i:]))
                    return answer

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
