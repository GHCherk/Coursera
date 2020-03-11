A = int(input())

if A == 1:
    n = 1
else:
    el1 = 0
    el2 = 1
    n = 2
    s = el1 + el2
    while s < A:
        el1, el2, s = el2, s, s + el2
        n += 1
    if s != A:
        n = -1
print(n)
