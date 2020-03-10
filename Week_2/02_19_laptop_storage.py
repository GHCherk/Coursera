A = int(input())
B = int(input())
C = int(input())
a = int(input())
b = int(input())
c = int(input())

n1 = (A//a) * (B//b) * (C//c)
n2 = (A//c) * (B//b) * (C//a)
n3 = (A//a) * (B//c) * (C//b)
n4 = (A//b) * (B//c) * (C//a)
n5 = (A//c) * (B//a) * (C//b)
n6 = (A//b) * (B//a) * (C//c)

n = 0
if n < n1:
    n = n1
if n < n2:
    n = n2
if n < n3:
    n = n3
if n < n4:
    n = n4
if n < n5:
    n = n5
if n < n6:
    n = n6
print(n)
