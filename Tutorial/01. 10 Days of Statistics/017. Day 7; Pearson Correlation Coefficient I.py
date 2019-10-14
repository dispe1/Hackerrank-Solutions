# Problem: https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
# Difficulty : Easy
# Score : 30

import statistics as st

n = int(input())

x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

mean_x = st.mean(x)
std_x = st.pstdev(x)

mean_y = st.mean(y)
std_y = st.pstdev(y)

correlation_coefficient = sum([(x[i] - mean_x) * (y[i] - mean_y ) for i in range(n)]) / (n * std_x * std_y)

print(round(correlation_coefficient,3))
