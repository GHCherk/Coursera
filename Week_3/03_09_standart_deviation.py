from math import sqrt

x = int(input())

if x == 0:
    quit()

n = 0
sumx2 = 0
sumx = 0
s = 0

while x != 0:
    n += 1
    sumx2 = sumx2 + x**2
    sumx = sumx + x
    x = int(input())
s = sumx / n
print(sqrt((sumx2 - 2 * s * sumx + n * (s**2)) / (n - 1)))
