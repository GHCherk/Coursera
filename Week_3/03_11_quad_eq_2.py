from math import sqrt

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        print(1, -c / b)
else:
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(2, min(x1, x2), max(x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        print(1, x)
    else:
        print(0)
