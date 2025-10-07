def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)

    return len(a_set) * 2 - 1



t = int(input())
for _ in range(t):
    print(solve())