# Problem: https://www.hackerrank.com/challenges/30-interfaces/problem
# Difficulty : Easy
# Score : 30

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([i if n % i == 0 else 0 for i in range(1, n+1)])

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
