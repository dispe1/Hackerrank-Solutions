# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Difficulty : Easy
# Score : 10

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [a + i for i in apples]
    oranges = [b + i for i in oranges]

    r = 0
    for i in apples:
        if s <= i <= t:
            r += 1
    print(r)
    r = 0
    for i in oranges:
        if s <= i <= t:
            r += 1
    print(r)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
