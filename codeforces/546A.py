k, n, w = map(int, input().split())
m = (w * (w + 1) // 2) * k
print(max(0, m - n))
