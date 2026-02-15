def solve():
    n = int(input())
    a = list(map(int, input().split()))

    aso = sorted(a)
    temp = -1

    freq = {}

    for i in range(n-1, -1, -1):
        freq[aso[i]] = i


    # print(freq)
    val = freq[a[0]]
    flag = False
    count = 0

    for i in range(n):
        if not flag and a[i] == aso[i]:
            count += 1
        else:
            val = max(val, freq[a[i]])
            flag = True
            freq[a[i]] += 1

        if flag and i >= val:
            flag = False
            count += 1

    return(count)




    # dec = 0

    # for i in range(1, n):
    #     if a[i] < a[i-1]:
    #         dec += 1

    # return n - dec



t = int(input())
for _ in range(t):
    print(solve())