# Problem: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Difficulty : Easy
# Score : 30

def median(ar):
    l = len(ar) // 2
    if len(ar) % 2 == 0:
        r = (ar[l] + ar[l-1]) / 2
    else:
        r = ar[l]
    print(int(r))

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
q = n // 2

left = l[:q]
right = l[-q:]


median(left)
median(l)
median(right)
