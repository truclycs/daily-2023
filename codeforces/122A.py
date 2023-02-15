lucky_num = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = int(input())
print("YES" if n in lucky_num or any(n % x == 0 for x in lucky_num) else "NO")
