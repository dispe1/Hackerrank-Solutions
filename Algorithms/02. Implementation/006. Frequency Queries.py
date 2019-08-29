# Problem: https://www.hackerrank.com/challenges/frequency-queries/problem
# Difficulty : Medium
# Score : 40

import os
import collections

def freqQuery(queries):
    arr = collections.Counter()
    result = []
    freq = collections.Counter()

    for q in queries:
        if q[0] == 1:
            freq[arr[q[1]]] -=1
            arr[q[1]] += 1
            freq[arr[q[1]]] +=1

        elif q[0] == 2 and arr[q[1]] > 0:
            freq[arr[q[1]]] -= 1
            arr[q[1]] -= 1
            freq[arr[q[1]]] += 1

        elif q[0] == 3:
            if freq[q[1]] > 0:
                result.append(1)
            else:
                result.append(0)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.close()
