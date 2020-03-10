l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())

if hc >= h1 + h2:
    if max(lc, wc) >= max(l1, w1) and max(lc, wc) >= max(l2, w2):
        if min(lc, wc) >= min(l1, w1) and min(lc, wc) >= min(l2, w2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
elif hc >= h1 and hc >= h2:
    if lc >= l1 + l2 and wc >= max(w1, w2):
        print("YES")
    elif lc >= l1 + w2 and wc >= max(w1, l2):
        print("YES")
    elif lc >= l2 + w1 and wc >= max(w2, l1):
        print("YES")
    elif lc >= w1 + w2 and wc >= max(l1, l2):
        print("YES")
    elif wc >= l1 + l2 and lc >= max(w1, w2):
        print("YES")
    elif wc >= l1 + w2 and lc >= max(w1, l2):
        print("YES")
    elif wc >= l2 + w1 and lc >= max(w2, l1):
        print("YES")
    elif wc >= w1 + w2 and lc >= max(l1, l2):
        print("YEs")
    else:
        print("NO")
else:
    print("NO")
