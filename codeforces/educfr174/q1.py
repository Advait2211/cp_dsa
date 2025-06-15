t = int(input())

for _ in range(t):
    length = int(input())

    array = list(map(int, input().split()))

    # print(length, array)

    if "101" in ''.join(map(str, array)):
        print("NO")
    else:
        print("YES")
