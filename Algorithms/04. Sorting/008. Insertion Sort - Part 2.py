# Problem: https://www.hackerrank.com/challenges/insertionsort2/problem
# Difficulty : Easy
# Score : 30

def insertionSort2(n, arr):
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = tmp

        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
