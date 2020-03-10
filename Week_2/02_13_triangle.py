import math
import sys

a = int(input())
b = int(input())
c = int(input())

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    print("impossible")
    sys.exit()

A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2)/(2 * a * c)))
C = 180 - A - B

if C > 0:
    if A == 90 or B == 90 or C == 90:
        print("rectangular")
    elif A < 90 and B < 90 and C < 90:
        print("acute")
    elif A > 90 or B > 90 or C > 90:
        print("obtuse")
else:
    print("impossible")
