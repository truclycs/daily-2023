n, t = map(int, input().split())
s = input()

for _ in range(t):
    res = ""
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            res += 'GB'
            i += 2
            continue
        res += s[i]
        i += 1
    if i == n - 1:
        res += s[i]
    s = res

print(res)
