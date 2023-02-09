n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
for x in a:
    if x >= a[k - 1] and x != 0:
        cnt += 1
print(cnt)
