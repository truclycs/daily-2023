n = int(input())
a = list(map(int, input().split()))
s = sum(a)
print("HARD" if s > 0 else "EASY")
