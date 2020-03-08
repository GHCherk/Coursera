N = int(input())
print(2**(abs(N // 1000 - N % 10) + abs(N % 1000 // 100 - N % 100 // 10)))
