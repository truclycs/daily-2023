s = input()
res = ""
s = s.lower()
for x in s:
    if x not in ['a', 'o', 'y', 'i', 'e', 'u']:
        res += '.' + x
print(res)
