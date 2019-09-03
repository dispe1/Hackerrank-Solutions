# Problem: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
# Difficulty : Medium
# Score : 35

def whatFlavors(cost, money):
    past = {}
    for idx in range(len(cost)):
        c = cost[idx]
        j = money- c
        if j in past:
            return str(past[j]) + " " + str(idx+1)
        if c not in past:
            past[c] = idx+1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        print(whatFlavors(cost, money))
