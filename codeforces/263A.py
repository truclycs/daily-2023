a = []
for _ in range(5):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
