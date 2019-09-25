# Problem: https://www.hackerrank.com/challenges/manasa-and-stones/problem
# Difficulty : Easy
# Score : 30

import os
def stones(n, a, b):
    ret = []

    for i in range(n):
        ret.append(a * i + b * (n - 1 -i))

    ret = list(set(ret))
    ret.sort()


    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())
        a = int(input())
        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
