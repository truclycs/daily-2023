s = input()
cnt = [0] * 26
for c in s:
    cnt[ord(c) - ord('a')] = 1
if sum(cnt) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
