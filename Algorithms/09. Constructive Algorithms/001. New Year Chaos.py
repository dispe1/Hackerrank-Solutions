# Problem: https://www.hackerrank.com/challenges/new-year-chaos/problem
# Difficulty : Medium
# Score : 40

def minimumBribes(q):
    r = 0

    for idx, number in enumerate(q):
        if number-(idx+1) > 2:
            print("Too chaotic")
            return;
        else:
            for k in range(max(number-2,0),idx):
                if q[k] > number:
                    r += 1
    print(r)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
