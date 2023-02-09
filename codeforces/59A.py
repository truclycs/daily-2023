s = input()
lower = sum(1 for x in s if x.islower())
print(s.upper() if len(s) - lower > lower else s.lower())
