from math import sqrt

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c)/2

S = sqrt(p * (p - a) * (p - b) * (p - c))

print(S)
