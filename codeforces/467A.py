n = int(input())
res = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b - a >= 2:
        res += 1
print(res)
