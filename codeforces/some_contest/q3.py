def solve():
    n = int(input())
    from collections import defaultdict, deque

    con = defaultdict(list)

    for _ in range(n-1):
        u, v = map(int, input().split())
        con[u].append(v)
        con[v].append(u)

    depth = {}
    q = deque([1])
    depth[1] = 0

    while q:
        u = q.popleft()
        for v in con[u]:
            if v not in depth:
                depth[v] = depth[u] + 1
                q.append(v)

    print(depth)

    

    



t = int(input())
for _ in range(t):
    print(solve())