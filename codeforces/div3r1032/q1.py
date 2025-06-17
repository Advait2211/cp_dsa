def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    first = a[0]
    last = a[-1]

    if s > first and s < last:
        base = min(s - first, last - s)
        return max(base + last - first, 0)
    elif s == first:
        return last - first
    elif s == last:
        return last - first
    elif s < first:
        return (last - s)
    elif s > last:
        return (s - first)

t = int(input())

for _ in range(t):
    print(solve())