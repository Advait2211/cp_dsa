# https://codeforces.com/problemset/problem/1799/B

"""

"""

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)

    if len(a_set) == 1:
        print(0)
        return
    
    if 1 in a_set:
        print(-1)
        return
    
    ops = []

    smallest = min(a)
    smallest_index = a.index(smallest)

    while True:
        changed = False

        for i in range(n):
            while a[i] > smallest:
                a[i] = (a[i] + smallest - 1) // smallest
                ops.append([i, smallest_index])
                changed = True

                if a[i] < smallest:
                    smallest = a[i]
                    smallest_index = i

        if not changed:
            break

    if len(set(a)) == 1:
        print(len(ops))
        for i, j in ops:
            print(i+1, j+1)
    else:
        print(-1)


t = int(input())

for _ in range(t):
    solve()
