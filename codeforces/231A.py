if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for _ in range(n):
        a, b, c = list(map(int, input().split()))
        if a + b + c >= 2:
            cnt += 1
    print(cnt)
