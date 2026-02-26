def solve():
    x, y = map(int, input().split())

    maxi = 0
    mini = 0

    if x % 2 == 0:
        maxi = x // 2
    else:
        maxi = x // 2 - 1

    if x % 4 == 0:
        mini = -1 * (x // 4)
    elif x % 4 == 1:
        mini = -1 * (x // 4) + 2
    elif x % 4 == 2:
        mini = -1 * (x // 4) + 1
    else:
        mini = -1 * (x // 4)

    # print(maxi, mini, maxi-mini)

    if y > maxi or y < mini:
        return "NO"

    if (maxi - y) % 3 == 0:
        return "YES"
    else:
        return "NO"

    

t = int(input())
for _ in range(t):
    print(solve())