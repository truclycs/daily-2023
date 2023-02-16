s = input()
hello = "hello"
i = 0
for c in s:
    if c == hello[i]:
        i += 1
        if i == len(hello):
            break
print("YES" if i == len(hello) else "NO")
