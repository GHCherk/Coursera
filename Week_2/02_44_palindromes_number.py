K = int(input())

i = 1
n = 0
num = 0
numnew = 0

while i <= K:
    num = i
    while num > 0:
        numnew = numnew * 10 + num % 10
        if num >= 10:
            num = num // 10
        else:
            num = 0
    if numnew == i:
        n += 1
    i += 1
    numnew = 0
print(n)
