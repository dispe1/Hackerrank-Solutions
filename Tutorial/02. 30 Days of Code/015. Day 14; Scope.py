# Problem: https://www.hackerrank.com/challenges/30-scope/problem
# Difficulty : Easy
# Score : 30

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
