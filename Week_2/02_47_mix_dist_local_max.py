i = int(input())
iprev2 = 0
iprev = 0
n = 1
nprev = 0
dist = 0
distprev = 0

while i != 0:
    iprev2, iprev = iprev, i
    i = int(input())
    if i == 0:
        break
    n += 1
    if iprev > iprev2 != 0 and iprev > i:
        if nprev != 0:
            distprev = dist
            dist = n - 1 - nprev
            if distprev != 0:
                dist = min(dist, distprev)
        nprev = n - 1
print(dist)
