a = int(input())
b = int(input())
c = int(input())

if c < b:
    n = b
    b = c
    c = n
if b < a:
    n = a
    a = b
    b = n
if c < b:
    n = b
    b = c
    c = n
print(a, b, c)
