# Problem: https://www.hackerrank.com/challenges/beautiful-triplets/problem
# Difficulty : Easy
# Score : 20

import os

def beautifulTriplets(d, arr):
    ret = 0
    l = len(arr)

    for i in range(l):
        for j in range(i+1, l):
            if arr[j] - arr[i] == d:
                for k in range(j+1, l):
                    if arr[k] - arr[j] == d:
                        ret += 1
                        break

                    elif arr[j] - arr[j] > d:
                        break
                break

            elif arr[j] - arr[i] > d:
                break

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result))
    fptr.close()
