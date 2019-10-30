# Problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Difficulty : Easy
# Score : 30

n = int(input())
d = {}

for i in range(n):
    k, v = input().split(' ')
    d[k] = v

try:
    while True:
        q = input()
        if q in d:
            print("{}={}".format(q, d[q]))
        else:
            print("Not found")
except EOFError:
    pass
