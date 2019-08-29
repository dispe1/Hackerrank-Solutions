# Problem: https://www.hackerrank.com/challenges/ctci-merge-sort/problem
# Difficulty : Hard
# Score : 45

import os

def countInversions(arr):
    return MergeSort(arr,0,len(arr)-1)

def MergeSort(arr, left, right):
    swap = 0
    if left < right:
        mid = (left + right) // 2
        swap += MergeSort(arr, left, mid)
        swap += MergeSort(arr, mid+1, right)
        swap += Merge(arr, left, mid, right)
    return swap

def Merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid+1
    swap = 0
    n = 0

    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            temp.append(arr[j])
            swap += (j-n-left)
            j += 1
        else:
            temp.append(arr[i])
            i += 1
        n += 1

    if i > mid:
        while j <= right:
            temp.append(arr[j])
            swap += (j-n-left)
            j += 1
            n += 1
    else:
        while i <= mid:
            temp.append(arr[i])
            i += 1
            n += 1

    arr[left:right+1] = temp

    return swap



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
