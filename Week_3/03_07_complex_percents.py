P = float(input())
X = int(input())
Y = int(input())
K = int(input())

i = 1
sum = X * 100 + Y + 10**(-9)

while i <= K:
    sum = int(sum + sum * P / 100)
    i += 1

print(int(sum // 100), int(sum % 100))
