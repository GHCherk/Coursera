i = int(input())
j = i
n = 0

while i != 0:
    if i > j:
        n = n + 1
    j = i
    i = int(input())
print(n)
