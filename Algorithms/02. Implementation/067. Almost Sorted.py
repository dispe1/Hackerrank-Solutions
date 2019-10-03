# Problem: https://www.hackerrank.com/challenges/almost-sorted/problem
# Difficulty : Medium
# Score : 50

def almostSorted(arr):
    sortedArr = sorted(arr)
    if sortedArr == arr:
        return "yes"

    n = len(arr)
    i, j = 0, n-1

    while i < n-1 and arr[i] < arr[i+1]:
        i += 1
    while j > 0 and arr[j-1] < arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]

    if sortedArr == arr:
        print("yes")
        print("swap {} {}".format(i+1, j+1))
        return

    l, r = i+1, j-1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    if sortedArr == arr:
        print("yes")
        print("reverse {} {}".format(i+1, j+1))
        return

    print("no")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
