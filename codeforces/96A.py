s = input()
zero = one = 0
dangerous = False
for x in s:
    if x == '0':
        zero += 1
        one = 0
    else:
        one += 1
        zero = 0

    if zero == 7 or one == 7:
        dangerous = True
        break

print("YES" if dangerous else "NO")
