# Problem: https://www.hackerrank.com/challenges/30-bitwise-and/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)
