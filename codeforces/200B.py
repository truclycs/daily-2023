n = int(input())
p = list(map(int, input().split()))

vol = 0
for x in p:
    vol += x / 100

print((vol / n) * 100)
