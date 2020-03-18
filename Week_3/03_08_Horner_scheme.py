n = int(input())
x = float(input())
i = 1
a = float(input())
aprev = 0
P = a

while i <= n:
    aprev = a
    a = float(input())
    P = P * x + a
    i += 1
print(P)
