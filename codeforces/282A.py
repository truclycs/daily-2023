n = int(input())
num = 0
for _ in range(n):
    x = input()
    num = num - 1 if '-' in x else num + 1
print(num)
