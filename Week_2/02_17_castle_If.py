A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if C > B:
    n = B
    B = C
    C = n
if B > A:
    n = A
    A = B
    B = n
if C > B:
    n = B
    B = C
    C = n
if E > D:
    n = D
    D = E
    E = n
if B <= D and C <= E:
    print("YES")
else:
    print("NO")
