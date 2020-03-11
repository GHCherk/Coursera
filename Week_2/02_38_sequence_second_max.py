max1 = int(input())
i = int(input())
max2 = i

if max1 < max2:
    max1, max2 = max2, max1

while i != 0:
    i = int(input())
    if i > max1:
        max2 = max1
        max1 = i
    elif max2 < i <= max1:
        max2 = i
print(max2)
