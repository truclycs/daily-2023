n, k = map(int, input().split())
if k <= (n - 1) // 2 + 1:
    print(k * 2 - 1)
else:
    k = k - ((n - 1) // 2 + 1)
    print(k * 2)
