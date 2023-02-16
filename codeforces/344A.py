n = int(input())
groups = 1
pre = input()
for _ in range(n - 1):
    cur = input()
    if cur != pre:
        groups += 1
    pre = cur
print(groups)
