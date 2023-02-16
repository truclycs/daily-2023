n = int(input())
a = list(map(int, input().split()))

s_all = sum(a)
min_coins = 0
a.sort()
s = 0
for x in a[::-1]:
    s += x
    min_coins += 1
    if s > s_all - s:
        break

print(min_coins)
