def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)

    max_diff = 0

    for i in range(0, n, 2):
        diff = a[i+1] - a[i]

        max_diff = diff if diff > max_diff else max_diff

    return max_diff




t = int(input())
for _ in range(t):
    print(solve())