A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())

if C1 > B1:
    n = B1
    B1 = C1
    C1 = n
if B1 > A1:
    n = A1
    A1 = B1
    B1 = n
if C1 > B1:
    n = B1
    B1 = C1
    C1 = n

if C2 > B2:
    n = B2
    B2 = C2
    C2 = n
if B2 > A2:
    n = A2
    A2 = B2
    B2 = n
if C2 > B2:
    n = B2
    B2 = C2
    C2 = n

if A1 == A2 and B1 == B2 and C1 == C2:
    print("Boxes are equal")
elif A1 <= A2 and B1 <= B2 and C1 <= C2:
    print("The first box is smaller than the second one")
elif A1 >= A2 and B1 >= B2 and C1 >= C2:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
