s = list(map(int, input().split()))
check = []
res = 0
for x in s:
    if x in check:
        res += 1
    check.append(x)
print(res)
