N = int(input())

Nnew = 0

while N > 0:
    Nnew = Nnew * 10 + N % 10
    if N >= 10:
        N = N // 10
    else:
        N = 0
print(Nnew)
