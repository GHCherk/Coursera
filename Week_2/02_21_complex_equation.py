a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print("INF")
elif b % a == 0 and (int(-b / a) * c + d) != 0:
    print(int(-b / a))
else:
    print("NO")
