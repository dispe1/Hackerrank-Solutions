# Problem: https://www.hackerrank.com/challenges/30-sorting/problem
# Difficulty : Easy
# Score : 30

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1

    if numberOfSwaps == 0:
        break

print(f"Array is sorted in {numberOfSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
