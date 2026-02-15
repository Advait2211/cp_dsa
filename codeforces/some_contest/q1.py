def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # ones = 0
    # flag = False

    # for val in a:
    #     if val == 1:
    #         if flag == True:
    #             pass
    #         else:
    #             flag = True
    #             ones += 1
    #     else:
    #         flag = False

    # print(ones)
    # if ones % 2 != 0:
    #     return("Alice")
    # else:
    #     return("Bob")

    if a[0] == 1 or a[-1] == 1:
        return "Alice"
    else:
        return "Bob"



t = int(input())
for _ in range(t):
    print(solve())