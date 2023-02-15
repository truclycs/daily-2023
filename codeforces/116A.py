n = int(input())

res = 0
cur = 0
for _ in range(n):
    a, b = map(int, input().split())
    cur = cur - a + b
    res = max(res, cur)
print(res)
