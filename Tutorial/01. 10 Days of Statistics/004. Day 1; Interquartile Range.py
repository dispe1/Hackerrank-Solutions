# Problem: https://www.hackerrank.com/challenges/s10-interquartile-range/problem
# Difficulty : Easy
# Score : 30

def median(arr):
    l = len(arr) // 2
    if len(arr) % 2 ==0:
        return (arr[l] + arr[l-1]) /2
    else:
        return arr[l]


n = int(input())
num = [int(i) for i in input().split()]
freq = [int(i) for i in input().split()]
d = {}

for i in range(n):
    if num[i] in d:
        d[num[i]] += freq[i]
    else:
        d[num[i]] = freq[i]

num = list(d.keys())
num.sort()

ar = []
for i in num:
    for j in range(d[i]):
        ar.append(i)

l = len(ar) // 2

left = ar[:l]
right = ar[-l:]
print(round(float(median(right) - median(left)),1))
