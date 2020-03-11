n = int(input())

if n == 1:
    s = 1
else:
    i = 2
    el1 = 0
    el2 = 1
    s = 0
    while i <= n:
        s = el1 + el2
        el1, el2 = el2, s
        i += 1
print(s)
