n, h = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for x in a:
    res += 1 if x <= h else 2
print(res)