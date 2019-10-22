# Problem: https://www.hackerrank.com/challenges/30-operators/problem
# Difficulty : Easy
# Score : 30

def solve(meal_cost, tip_percent, tax_percent):
    r = meal_cost + meal_cost * (tip_percent+tax_percent) / 100
    print(round(r))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
