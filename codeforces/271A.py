def is_distinct_digits(n):
    cnt = [0] * 10
    cnt[n // 1000] += 1
    cnt[n % 10] += 1
    cnt[(n % 100) // 10] += 1
    cnt[(n // 100) % 10] += 1
    return all(x <= 1 for x in cnt)


n = int(input())
n += 1
while not is_distinct_digits(n):
    n += 1

print(n)
