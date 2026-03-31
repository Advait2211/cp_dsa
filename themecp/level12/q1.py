# https://codeforces.com/problemset/problem/1728/A

"""

"""

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    num = max(a)
    where_num = a.index(num)

    return where_num+1

t = int(input())

for _ in range(t):
    print(solve())
