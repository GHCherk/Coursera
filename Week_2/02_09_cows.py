n = int(input())
if 11 <= n <= 19 or 5 <= n % 10 <= 9 or n % 10 == 0:
    k = "korov"
elif n % 10 == 1:
    k = "korova"
else:
    k = "korovy"
print(n, k)
