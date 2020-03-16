from math import floor
P = float(input())
X = int(input())
Y = int(input())

sum = (X * 100 + Y) * (1 + P / 100) + 10**(-9)

print(int(sum // 100), int(sum % 100))
