n = int(input())
res = ""
words = ["hate", "love"]
for i in range(n):
    res += "I " + words[i % 2] + " "
    if i != n - 1:
        res += "that "
print(res + "it")
