c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if r2 > r1 and (r2 - r1) % 2 == abs(c2 - c1) % 2:
    print("YES")
else:
    print("NO")
