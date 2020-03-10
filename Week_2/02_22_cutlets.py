k = int(input())
m = int(input())
n = int(input())

if n == 0:
    N = 0
elif n <= k:
    N = m * 2
else:
    N = ((2 * n - 1) // k + 1) * m
print(N)
