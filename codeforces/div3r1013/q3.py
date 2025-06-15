def solve():
    n = int(input())

    # fuck this was easy
    
    if n % 2 == 0:
        print(-1)
    else:
        print(*[i for i in range(n, 0, -1)])

t = int(input())

for _ in range(t):
    solve()