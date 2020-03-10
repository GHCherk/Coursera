a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    n = 3
elif a == b or a == c or b == c:
    n = 2
else:
    n = 0
print(n)
