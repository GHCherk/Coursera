N = int(input())
N = N % (3600 * 24)
print(N // 3600, ":", N % 3600 // 600, N % 600 // 60, ":", sep="", end="")
print(N % 60 // 10, N % 10, sep="")
