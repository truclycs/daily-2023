n = int(input())
if n % 2 == 0:
    n //= 2
    print(n * (n + 1) - n ** 2)
else:
    n //= 2
    print(n * (n + 1) - (n + 1) ** 2)
