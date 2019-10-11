# Problem: https://www.hackerrank.com/challenges/countingsort4/problem
# Difficulty : Medium
# Score : 40

def countSort(arr):
    n = len(arr)
    ret = [[] for _ in range(n // 2 + 1) ]

    for i in range(n):
        if i < n // 2:
            arr[i][1] = '-'

        ret[int(arr[i][0])].append(arr[i][1])

    ret = [' '.join(i) for i in ret if not len(i) == 0]

    print(' '.join(ret))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
