i = int(input())
m = i
if i == 0:
    n = 0
else:
    n = 1

while i != 0:
    i = int(input())
    if m < i:
        m = i
        n = 1
    elif m == i:
        n += 1
print(n)
