def solve():
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    sm = sum(a)

    if sm > s:
        return "NO"

    if (s - sm) % x == 0:
        return "YES"
    else:
        return "NO"
    



t = int(input())
for _ in range(t):
    print(solve())