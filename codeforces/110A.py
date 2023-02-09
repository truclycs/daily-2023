def is_lucky_number(n):
    if n == 0:
        return False
    while n != 0:
        if n % 10 not in [4, 7]:
            return False
        n //= 10
    return True


n = int(input())
cnt = 0
while (n != 0):
    if is_lucky_number(n % 10):
        cnt += 1
    n //= 10

print("YES" if is_lucky_number(cnt) else "NO")
