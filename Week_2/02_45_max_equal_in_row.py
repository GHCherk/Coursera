i = int(input())
iprev = i

n = 0
nmax = 0

while i != 0:
    if i == iprev:
        n += 1
        nmax = max(n, nmax)
    else:
        n = 1
    iprev = i
    i = int(input())
print(nmax)
