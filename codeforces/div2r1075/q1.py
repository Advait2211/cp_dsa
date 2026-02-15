def solve():
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    lth = 0
    ltl = 0

    for val in a:
        if val <= h:
            lth += 1
        if val <= l:
            ltl += 1


    if lth == ltl:
        return lth // 2
    

    # print(lth, ltl)

    diff = max(lth, ltl) - min(lth, ltl)

    ans = diff
    mini = min(lth, ltl)

    if diff > mini:
        return mini
    else:
        mini -= diff
        ans += mini // 2
        return ans




t = int(input())
for _ in range(t):
    print(solve())