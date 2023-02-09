n = int(input())
s = input()
a = sum(1 for x in s if x == 'A')
if a > n - a:
    print("Anton")
elif a < n - a:
    print("Danik")
else:
    print("Friendship")
