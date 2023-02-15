def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def binary_search(a, left, right, value):
    mid = (left + right) // 2
    while left <= right:
        if a[mid] < value:
            left = mid + 1
        elif a[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1
